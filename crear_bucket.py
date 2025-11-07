import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
  
    body = event['body'] if isinstance(event['body'], dict) else json.loads(event['body'])
    bucket_name = body['bucket']

    try:
        s3.create_bucket(Bucket=bucket_name)
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': f'Bucket "{bucket_name}" creado correctamente.'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

