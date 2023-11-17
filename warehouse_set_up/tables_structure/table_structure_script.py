import os
import yaml
import psycopg2 
from pathlib import Path

print('table_structure_started')

conn = psycopg2.connect( 
    database=os.getenv('POSTGRES_DB'), user=os.getenv('POSTGRES_USER'),  
  password=os.getenv('POSTGRES_PASSWORD'), host='portifolio_postgres_db', port=5432
) 
print(conn)
conn.autocommit = True
cursor = conn.cursor() 
path = Path(__file__).parent.absolute()
directory = f'{path}/yamls'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        with open(f, 'r') as file:
            file_info = yaml.safe_load(file)
            if(file_info != None):
                schema = file_info['destination_schema']
                sql_schema = f'CREATE SCHEMA IF NOT EXISTS {schema}; '
                cursor.execute(sql_schema)
                for each_table in file_info['tables']:
                    query = f'CREATE TABLE {schema}.{each_table["name"]}('
                    table_name = each_table['name']
                    for each_column in each_table['fields']:
                        query = query + f'{each_column["column_name"]} varchar,'
                    query = query[:-1] + ');'
                    cursor.execute(query) 
                    print(query)
conn.commit() 
conn.close() 