# aws_connector.py

import boto3

def get_iam_client():
    # Initialize and return the IAM client
    return boto3.client('iam')
