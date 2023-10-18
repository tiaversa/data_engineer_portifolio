FROM apache/airflow:2.7.2
COPY requirements.txt /
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
COPY tables_structure tables_structure
COPY docker_entry_point/table_structure_script.py docker-entrypoint-initdb.d/table_structure_script.py