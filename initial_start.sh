# Check if docker is running;
if ! docker info >/dev/null 2>&1; then
    echo "Docker does not seem to be running, run it first and retry"
    exit 1
fi

echo "Spinning up local Airflow infrastructure"
rm -rf logs
mkdir logs
rm -rf temp
mkdir temp
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
docker compose up airflow-init
docker compose up -d
echo "Sleeping 2 Minutes to let Airflow containers reach a healthy state"
sleep 120

echo "Spinning up postgres inside airflow"
docker exec -d gl_airflow-webserver_1 airflow connections add 'postgres_default' --conn-type 'Postgres' --conn-login 'airflow' --conn-password 'airflow' --conn-host 'localhost' --conn-port 5432 --conn-schema 'airflow'

echo "spinning up second postgres DB"
docker run --name postgresY -e POSTGRES_PASSWORD=postgres --mount source=postgresY,target=/var/lib/postgresql/data -p 1234:5432 -d postgres:13

echo "adding postgres 2 to airflow connection"
docker exec -d gl_airflow-webserver_1 airflow connections add 'postgresY' --conn-type 'Postgres' --conn-login 'postgres' --conn-password 'postgres' --conn-host 'localhost' --conn-port 1234 --conn-schema 'postgres'

echo "Successfully setup local Airflow, postgres 1, and postgres 2"