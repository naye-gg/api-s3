import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    bucket = body['bucket']
    directorio = body['directorio']


    try:
        key = f"{directorio.strip('/')}/"
        s3.put_object(Bucket=bucket, Key=key)
        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': f'Directorio "{directorio}" creado en bucket "{bucket}".'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

