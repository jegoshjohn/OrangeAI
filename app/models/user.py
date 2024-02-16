from pydantic import BaseModel, EmailStr, Field
# User object is a data model that represents a user in the application. 

class User(BaseModel):
    email_id: EmailStr = Field()
    """email: Email address of the user"""
    first_name: str
    """first_name: First name of the user"""
    last_name: str
    """last_name: Last name of the user"""

    def __str__(self):
        return f"User: {self.email_id}, {self.first_name}, {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

