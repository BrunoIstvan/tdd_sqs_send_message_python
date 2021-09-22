import boto3
import os

SQS_QUEUE_URL = os.getenv('SQS_QUEUE_URL', 'URL da fila não informada')


class SQSService(object):

    def get_client(self):
        return boto3.client('sqs')

    def execute_send_message(self, sqs_client, message):
        response = sqs_client.send_message(QueueUrl=SQS_QUEUE_URL, MessageBody=message)
        return response['MessageId']
