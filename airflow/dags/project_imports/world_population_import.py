import os
import boto3
import requests
import pandas as pd
from datetime import datetime, timedelta
# from tolls import *

def export_excel_file():
    """
    Test if dag works on new structure

    Parameters
    ----------
    text : string
        string to test result.
    """
    print('Start of export')
    url = "https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/EXCEL_FILES/1_General/WPP2022_GEN_F01_DEMOGRAPHIC_INDICATORS_REV1.xlsx"
    print('call function')
    time = datetime.now()
    import_online_file_to_s3(url,'world-population-timna-portifolio',
    f'{time.year}/{time.month}/{time.day}/world_population_{time.year}_{time.month}_{time.day}.xlsx')
    print("End of export")

def import_online_file_to_s3(url, bucket_name, object_key):
  """Imports an files from the internet into an S3 bucket.

  Args:
    url: The URL of the file.
    bucket_name: The name of the S3 bucket.
    object_key: The key of the object in the S3 bucket.
  """
  s3 = boto3.client('s3')
  print(s3)
  response = requests.get(url)
  s3.put_object(Bucket=bucket_name, Key=object_key, Body=response.content)
  df = pd.read_csv(f's3://{bucket_name}/{object_key}')
  print(df)

def read_from_s3_to_pd(bucket_name, object_key):
  s3 = boto3.client('s3')
  print(s3)
  df = pd.read_csv(f's3://{bucket_name}/{object_key}')
  print(df)

def load_into_postgres():
  print('Start of Load')
  time = datetime.now()
  read_from_s3_to_pd('world-population-timna-portifolio',
  f'{time.year}/{time.month}/{time.day}/world_population_{time.year}_{time.month}_{time.day}.xlsx')
  print("End of Load")