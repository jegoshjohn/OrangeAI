from models.chat import AIChatInput
from clients.dynamodb import DynamoDBClient
from utils.common import logger
import os

class ChatDao:
    def __init__(self):
        self.db: DynamoDBClient = DynamoDBClient(table_name=os.getenv("DYNAMODB_TABLE_NAME_CHAT"))

    def create_chat(self, chat_msg: AIChatInput)-> dict:
        self.db.put_item(chat_msg.dict())
        return chat_msg.dict()
    
    def get_chats_by_user(self, email_id)-> list:
        chat_msgs = self.db.query_items("email_id", email_id, "chat_msg")
        if chat_msgs:
            logger.info(f"Chat messages found: {chat_msgs}")
            return chat_msgs[0]["chat_msg"]
        else:
            logger.info(f"No chat messages found for email: {email_id}")
            return []
        
    def delete_chats_by_user(self, email_id):
        chat_msgs = self.db.query_items("email_id", email_id, "email_id, chat_ts")
        items_deleted = 0
        if chat_msgs:
            for chat_msg in chat_msgs:
                items_deleted += 1
                self.db.delete_item({"email_id": chat_msg["email_id"], "chat_ts": chat_msg["chat_ts"]})
            return {"message": "Chats deleted successfully", "items_deleted": items_deleted}
        else:
            return {"message": "No chats found for deletion"}