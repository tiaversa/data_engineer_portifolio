FROM apache/airflow:2.7.2
COPY requirements.txt /

RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt

COPY tables_structure tables_structure
COPY docker_entry_point/table_structure_script.py docker-entrypoint-initdb.d/table_structure_script.py
