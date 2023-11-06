import boto3, requests
import inspect, sys
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

def read_from_s3_to_pd(bucket_name, object_key,region_name='eu-west-1'):
  s3 = boto3.client("s3", region_name=region_name)
  try:
      res = s3.get_object(Bucket=bucket_name, Key=object_key)
  except botocore.exceptions.ClientError as e:
      if e.response["Error"]["Code"] == "NoSuchKey":
          file_data = None
          print('No Such Key Found')
      else:
          raise
  else:
      file_data = res["Body"].read()
  return file_data

if __name__ == '__main__':
    print ('aws script called.')