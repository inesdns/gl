echo "Spinning down local Airflow infrastructure"
docker compose down --volumes --rmi all

echo "Spinning down postgres"
docker kill postgresY
docker rm postgresY
docker volume rm postgresY

echo "Airflow and Postgres has been removed"