import boto3
import requests
from datetime import datetime

def import_online_file_to_s3(url, bucket_name, object_key):
  """Imports an files from the internet into an S3 bucket.

  Args:
    url: The URL of the file.
    bucket_name: The name of the S3 bucket.
    object_key: The key of the object in the S3 bucket.
  """
  s3 = boto3.client('s3')
  response = requests.get(url)
  s3.put_object(Bucket=bucket_name, Key=object_key, Body=response.content)

def say_hi():
    print('hi')
