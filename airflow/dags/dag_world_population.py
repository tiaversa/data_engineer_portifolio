from datetime import datetime, timedelta
import json

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator

import project_imports.world_population_import as project_import

# world_population_file_url = Variable.get("world_population_file_url")
world_population_file_url = 'https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_General/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx'
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
    op_kwargs={
            "url":world_population_file_url
        },
    dag=dag,
)

load_into_postgres = PythonOperator(
    task_id=f"load_into_postgres",
    python_callable=project_import.load_into_postgres,
    trigger_rule="all_success",
    dag=dag,
)
export_excel >> load_into_postgres
