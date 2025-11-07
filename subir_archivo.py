import boto3
import base64
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    body = json.loads(event['body'])
    
    bucket = body['bucket']
    directorio = body['directorio']
    nombre_archivo = body['nombre_archivo']
    contenido_base64 = body['contenido']

    try:
        contenido = base64.b64decode(contenido_base64)
        key = f"{directorio.strip('/')}/{nombre_archivo}"

        s3.put_object(Bucket=bucket, Key=key, Body=contenido)

        return {
            'statusCode': 200,
            'body': json.dumps({'mensaje': f'Archivo "{nombre_archivo}" subido a "{directorio}" en bucket "{bucket}".'})
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }

