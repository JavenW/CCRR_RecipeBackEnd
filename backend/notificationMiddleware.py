import requests
import os
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')


class notification_middleware:

    def __int__(self):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """

        AWS_REGION = "us-east-1"
        self.sns_client = boto3.client("sns", region_name=AWS_REGION)
        self.topic = os.environ.get("topicArn")
        
    def publish_message(self, subject, message):
        """
        Publishes a message, with attributes, to a topic. Subscriptions can be filtered
        based on message attributes so that a subscription receives messages only
        when specified attributes are present.

        :param topic: The topic to publish to.
        :param message: The message to publish.
        :return: The ID of the message.
        """
        try:
            response = self.sns_client.publish(
                TopicArn=self.topic,
                Message=message,
                Subject=subject,
            )['MessageId']

        except ClientError:
            logger.exception(f'Could not publish message to the topic.')
            raise
        else:
            return response

        