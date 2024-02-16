# Client Implementation for DynamoDB operations

from models.user import User
import boto3
from botocore.exceptions import ClientError
from typing import List, Optional
from boto3.dynamodb.conditions import Key
import os
from utils.common import logger

class DynamoDBClient:
    def __init__(self, table_name: str):
        self.client = boto3.resource('dynamodb', region_name=os.getenv("AWS_REGION", "us-east-1"))
        self.table = self.client.Table(table_name)

    def get_item(self, item_id: str, key_id: str) -> Optional[dict]:
        try:
            response = self.table.get_item(Key={key_id: item_id})
            if "Item" in response:
                return response["Item"]
            else:
                return None
        except ClientError as e:
            logger.info(e.response['Error']['Message'])
            raise e
    
    def query_items(self, key_id: str, key_value: str, projection: str | None) -> list:
        try:
            response = self.table.query(
                KeyConditionExpression=Key(key_id).eq(key_value),
                ProjectionExpression=projection
            )
            logger.info(f"Query response: {response}")
            return response["Items"]
        except ClientError as e:
            print(e.response['Error']['Message'])
        return []
    
    def scan_items(self) -> list:
        try:
            response = self.table.scan()
            return response["Items"]
        except ClientError as e:
            print(e.response['Error']['Message'])
        return []
    
    def put_item(self, item: dict):
        try:
            self.table.put_item(Item=item)
        except ClientError as e:
            if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
                logger.info(e.response['Error']['Message'])
                logger.info(f"Item already exists: {item}")
            else:
                raise e

    def update_item(self, item_id: str, key_id: str, update_expression: str, expression_attribute_values: dict):
        try:
            self.table.update_item(
                Key={key_id: item_id},
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values
            )
        except ClientError as e:
            print(e.response['Error']['Message'])

    def delete_item(self, key_expr: dict):
        try:
            self.table.delete_item(Key=key_expr)
        except ClientError as e:
            print(e.response['Error']['Message'])
