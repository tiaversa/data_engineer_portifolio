from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {'start_date': airflow.utils.dates.days_ago(2)}

with DAG('my_dag', default_args=default_args, schedule_interval='@daily') as dag:

    read_file = BashOperator(
        task_id='read_file',
        bash_command='cat /opt/airflow/external_volume/my_file.txt',
    )

    read_file