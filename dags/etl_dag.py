from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
import datetime

with DAG(
    dag_id="etl_glints",
    start_date=datetime.datetime(2021, 9, 10),
    schedule_interval="@once",
    max_active_runs=1,
) as dag:

    etl2 = BashOperator(
        task_id="etl2",
        bash_command=f'python /opt/airflow/dags/main_final.py',
    )

    etl2