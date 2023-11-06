# import sys
# sys.path.insert(0,os.path.abspath(os.path.dirname(__file__)))
# import os
import boto3
import requests
import pandas as pd
from datetime import datetime, timedelta
import tolls.aws as aws

def export_excel_file(url):
  """
  Test if dag works on new structure

  Parameters
  ----------
  text : string
      string to test result.
  """
  print('Start of export')
  time = datetime.now()
  aws.import_online_file_to_s3(url,'world-population-timna-portifolio',
  f'{time.year}/{time.month}/{time.day}/world_population_{time.year}_{time.month}_{time.day}.xlsx')
  print("End of export")

def load_into_postgres():
  print('Start of Load')
  time = datetime.now()
  file_data = aws.read_from_s3_to_pd('world-population-timna-portifolio',
  f'{time.year}/{time.month}/{time.day}/world_population_{time.year}_{time.month}_{time.day}.xlsx')
  df = pd.read_excel(file_data)
  print(df)
  print("End of Load")