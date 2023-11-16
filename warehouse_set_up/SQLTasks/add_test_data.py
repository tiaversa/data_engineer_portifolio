print('at least started')
import pandas as pd
import os, psycopg2, time, pathlib
from sqlalchemy import create_engine

path = pathlib.Path(__file__).parent.resolve()
print('add_test_data_started')
conn_str = (f"postgresql://{os.getenv('POSTGRES_USER')}:"\
                        f"{os.getenv('POSTGRES_PASSWORD')}@portifolio_postgres_db:"\
                        f"5432/{os.getenv('POSTGRES_DB')}")
print(conn_str)
engine = create_engine(conn_str)

files_list = os.listdir(path)
print(files_list)
for file_name in files_list:
    if 'Data.xlsx' in file_name:
        name = '_'.join(file_name.split('_')[:-1])
        print(f"Loading {file_name} to Data Warehouse Portifolio.")
        try:
            df = pd.read_excel(str(path) + "/" + file_name)
            df.to_sql(name,engine,if_exists="append",index=False,schema='sql_test')
        except Exception as e:
            print(f"Error occurred while loading {name} in Data Warehouse: {e}.")

        print(f"Loading {file_name} finalized.")