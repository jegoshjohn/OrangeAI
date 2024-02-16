from fastapi import APIRouter
from utils.common import logger
from api.v1.endpoints import users, chats

logger.info("Starting the TOP Level API router")
api_router = APIRouter()
api_router.include_router(users.router, tags=["User"])
api_router.include_router(chats.chat_router, tags=["Chat"])