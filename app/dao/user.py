from models.user import User
from clients.dynamodb import DynamoDBClient
from utils.common import logger
import os

class UserDao:
    def __init__(self):
        self.db: DynamoDBClient = DynamoDBClient(table_name=os.getenv("DYNAMODB_TABLE_NAME"))

    def get_user_by_email(self, email_id):
        user: User = self.db.get_item(email_id, "email_id")
        if user:
            logger.info(f"User found: {user}")
            return user
        else:
            logger.info(f"User not found with email: {email_id}")
            return {}

    def create_user_in_db(self, user: User) -> dict:
        self.db.put_item(user.dict())
        return self.get_user_by_email(user.email_id)