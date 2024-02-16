from models.user import User
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dao.user import UserDao
from utils.common import logger


router = APIRouter()

logger.info("Starting the USER API router")

@router.get("/user/{email_id}")
async def get_user(email_id):
    logger.info(f"Fetching user with email: {email_id}")
    return JSONResponse(UserDao().get_user_by_email(email_id))

@router.put("/user")
async def create_user(user: User):
    logger.info(f"Payload: {user}")
    logger.info(f"Payload DICT: {user.dict()}")
    persisted_user = UserDao().create_user_in_db(user)
    logger.info(f"User created: {persisted_user}")
    return JSONResponse(persisted_user)
    