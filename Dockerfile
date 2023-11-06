FROM python:3.12

COPY requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /requirements.txt


CMD ["python3", "home/tables_structure/table_structure_script.py"]