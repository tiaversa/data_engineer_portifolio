from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

def ext_load_taxi():
    print('hi')

dag = DAG(
    "NY_taxi_pipeline",
    schedule_interval="1 1 1 * *",
    default_args={
        "start_date":datetime(2023,11,12)
    },
    tags=["taxi","pyspark"]
)

ext_load = PythonOperator(
    task_id="ext_load",
    python_callable=ext_load_taxi,
    dag=dag,
)