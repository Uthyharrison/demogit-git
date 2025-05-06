mport boto3
import os
import json
import uuid
import datetime
import urllib3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Set environment variables in Lambda console
DYNAMODB_TABLE = os.environ['DYNAMODB_TABLE']
SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

http = urllib3.PoolManager()

def lambda_handler(event, context):
        for record in event['Records']:
                    s3_info = record['s3']
                            bucket_name = s3_info['bucket']['name']
                                    object_key = s3_info['object']['key']

                                            # Only proceed for .html files
                                                    if not object_key.lower().endswith('.html'):
                                                                    return {"statusCode": 200, "body": "File is not HTML. Ignored."}

                                                                        file_url = f"https://{bucket_name}.s3.amazonaws.com/{object_key}"
                                                                                upload_time = datetime.datetime.utcnow().isoformat()

                                                                                        # Send SNS notification
                                                                                                sns_message = f"New HTML file uploaded: {object_key} at {upload_time}"
                                                                                                        sns.publish(
                                                                                                                            TopicArn=SNS_TOPIC_ARN,
                                                                                                                                        Message=sns_message,
                                                                                                                                                    Subject="New HTML Upload Notification"
                                                                                                                                                            )

                                                                                                                # Save metadata to DynamoDB
                                                                                                                        table = dynamodb.Table(DYNAMODB_TABLE)
                                                                                                                                table.put_item(Item={
                                                                                                                                                'id': str(uuid.uuid4()),
                                                                                                                                                            'filename': object_key,
                                                                                                                                                                        'bucket': bucket_name,
                                                                                                                                                                                    'url': file_url,
                                                                                                                                                                                                'timestamp': upload_time
                                                                                                                                                                                                        })

                                                                                                                                        # Send Slack alert
                                                                                                                                                slack_payload = {
                                                                                                                                                                    "text": f":globe_with_meridians: *New HTML File Uploaded!*\n*File:* {object_key}\n*Bucket:* {bucket_name}\n*Time:* {upload_time}\n*URL:* {file_url}"
                                                                                                                                                                            }
                                                                                                                                                        encoded_data = json.dumps(slack_payload).encode('utf-8')
                                                                                                                                                                 http.request('POST', SLACK_WEBHOOK_URL, body=encoded_data, headers={'Content-Type': 'application/json'})

                                                                                                                                                                     return {"statusCode": 200, "body": "Notification and logging complete."}

