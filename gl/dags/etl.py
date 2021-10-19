from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.dummy_operator import DummyOperator
from scripts.operators.pgtopg import PostgresToPostgresOperator
import datetime

with DAG(
    dag_id="postgres_operator_dag",
    start_date=datetime.datetime(2021, 11, 18),
    schedule_interval='@once',
) as dag:

    extract_sales_to_target = PostgresToPostgresOperator(
        task_id="extract_sales_to_target",
        source_postgres_conn_id="postgres_default",
        target_postgres_conn_id="postgresY",
        sql='''SELECT * FROM retail.user_purchase
                '''
    )
extract_sales_to_target