# Prerequisites
- Install [Docker](https://www.docker.com/)
- Install [Docker Compose](https://docs.docker.com/compose/install/)
- git clone https://github.com/inesdns/gl.git
- install requirement.txt

# Usage
## Setup
If you are running this code for the first time, please run the `initial_start.sh` script
```
chmod +x initial_start.sh && ./initial_start.sh
```
This script will set up your environment:
- Airflow 2.1
- PostgresY as the secondary database
- Load sample database to primary database
- Create necessary folder

After that you can run `chmod +x start.sh && ./start.sh` or `docker-compose up -d && docker start postgresY`
This will start Airflow and our secondary database (postgresY)

## Databases
Since the sample data is small, I put primary database using Airflow metadata database (Postgres on port 5432) and the secondary database on port 1234. Both run on docker and will use `host.docker.internal` as their host
The sample data will be automatically loaded on our primary database.

Credential:
```
DB 1
host = host.docker.internal
Port = 5432
Username = airflow
Password = airflow
```
Data on DB 1 located on `airflow.retail.user_purchase`

```
DB 2
host = host.docker.internal
Port = 1234
Username = postgres
Password = postgres
```
Data on DB 2 located on `test.retail.user_purchase`

## Checking Data
please run `docker exec -e "PGOPTIONS=--search_path=retail" -it postgresY psql -U postgres test`
Sample query to inspect the data of secondary database (target database):

```
select * from retail.user_purchase limit 5;
select count(*) from retail.user_purchase;
```

If you want to check the data from primary database, please run
`docker exec -e "PGOPTIONS=--search_path=retail" -it gl_postgres_1 psql -U airflow airflow`
You can run the same queries as above to compare value

## DAG
Check http://localhost:5884
username : `airflow`
password : `airflow`

## Tearing down
To tear down, please run `chmod +x teardown.sh && ./teardown.sh` This will stop and remove airflow and postgresY

