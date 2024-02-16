import datetime
from pydantic import BaseModel, EmailStr, Field

class AIChatInput(BaseModel):
    chat_msg: str
    """chat_msg: Message sent by the user"""
    email_id: EmailStr = Field()
    """email_id: Unique identifier for the user"""
    chat_ts: str | None = datetime.datetime.now().isoformat()
    """chat_msg: Time when the message was sent"""

class AIChat(BaseModel):
    chat_id: str
    """chat_id: Unique identifier for the chat"""
    email_id: EmailStr = Field()
    """email_id: Unique identifier for the user"""
    chat_msg: str
    """message: Message sent by the user"""
    chat_ts: str
    """chat_msg: Time when the message was sent"""
    def __str__(self):
        return f"Chat: {self.chat_id}, {self.email_id}, {self.chat_msg}, {self.timestamp}"
    
class AIChatHistory(BaseModel):
    chats: list[AIChat]

class AIChatDeleteRequest(BaseModel):
    email_id: EmailStr = Field()
    """email_id: Unique identifier for the user"""