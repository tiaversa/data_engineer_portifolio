from datetime import datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

import project_imports.world_population_import as project_import

dag = DAG(
    "world_population_pipeline_dag",
    catchup=False,
    schedule_interval="* 1 1 * *",
    default_args={
        "start_date": datetime(2023, 10, 19),
    },
    tags=["world_population", "excel"]
)

export_excel = PythonOperator(
    task_id=f"export_excel",
    python_callable=project_import.export_excel_file,
    dag=dag,
)