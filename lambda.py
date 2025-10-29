import json
import boto3

sns = boto3.client('sns')
TOPIC_ARN = 'arn:aws:sns:ap-south-1:350235531785:event-announcements'

def lambda_handler(event, context):
    try:
        # Parse the request body
        body = json.loads(event['body'])
        event_name = body.get('event_name')
        description = body.get('description')

        # Create message
        message = f"📢 New Event: {event_name}\nDetails: {description}"

        # Publish to SNS topic
        sns.publish(
            TopicArn=TOPIC_ARN,
            Message=message,
            Subject=f"Event Announcement: {event_name}"
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Event published successfully!'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
