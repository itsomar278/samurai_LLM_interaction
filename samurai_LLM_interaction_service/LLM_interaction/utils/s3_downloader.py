import os
import boto3
from botocore.config import Config
from botocore.exceptions import NoCredentialsError
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()


def download_s3_file(s3_file_url):
    print("im here")
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = os.getenv('AWS_REGION')
    s3_bucket_name = os.getenv('S3_BUCKET_NAME')

    if not all([aws_access_key_id, aws_secret_access_key, aws_region, s3_bucket_name]):
        raise ValueError("AWS credentials or bucket name are not set in environment variables.")

    file_key = s3_file_url.split(f'https://{s3_bucket_name}.s3.amazonaws.com/')[1]
    print("i reached line 22 ")

    boto_config = Config(
        region_name=aws_region,
        retries={'max_attempts': 10, 'mode': 'standard'},
        max_pool_connections=1
    )

    session = boto3.session.Session()
    print("i reached line 30 ")
    s3_client = session.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        config=boto_config
    )

    try:
        print("i reached line 38 ")
        file_buffer = BytesIO()
        s3_client.download_fileobj(s3_bucket_name, file_key, file_buffer)
        print("i reached line 40 ")
        file_buffer.seek(0)

        print(f"File downloaded successfully from {s3_file_url}")
        return file_buffer.getvalue()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    finally:
        print("i reached the finally statement")