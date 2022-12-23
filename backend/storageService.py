import pymysql
import os
import boto3


class StorageService:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("DBUSER")
        # pw = os.environ.get("DBPW")
        # h = os.environ.get("DBHOST")
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('Storage')

        return table

    @staticmethod
    def insert_item(email, item, expired_date):

        table = StorageService._get_connection()
        items = StorageService.get_items(email)
        items[item] = expired_date
        table.put_item(
            Item={
                'email': email,
                'items': items
            }
        )

    @staticmethod
    def get_items(email):
        try:
            table = StorageService._get_connection()
            response = table.get_item(
                Key={
                    'email': email
                }
            )
            if 'Item' in response:
                return response['Item']['items']
            return {}
        except:
            return {}

    @staticmethod
    def remove_item(email, item):

        table = StorageService._get_connection()
        items = StorageService.get_items(email)
        items.pop(item, None)
        table.put_item(
            Item={
                'email': email,
                'items': items
            }
        )


# StorageService.insert_item("11112",'apple', '4567')
# print(StorageService.get_items("jw4156@columbia.edu"))
# StorageService.remove_item("11111","apple")


# client = boto3.client('ses')
# res = client.list_identities(
#     IdentityType='EmailAddress'
# )
# print(res['Identities'])

