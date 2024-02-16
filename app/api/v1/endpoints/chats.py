import datetime
from dao.user import UserDao
from models.chat import AIChatDeleteRequest, AIChatInput
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from dao.chat import ChatDao
from utils.common import logger
from api.ai.gemini import GeminiAI


chat_router = APIRouter()

logger.info("Starting the CHAT API router")


@chat_router.post("/chat")
async def create_chat(chat_payload: AIChatInput):
    """Create a chat message with historical context for the user

    Args:
        chat_payload (AIChatInput): The chat payload

    Returns:
        _type_: _description_
    """
    # Validate the user
    user_id = UserDao().get_user_by_email(chat_payload.email_id)
    if not user_id:
        return JSONResponse({"error": "User not found"}, status_code=400)
    chat_history = ChatDao().get_chats_by_user(chat_payload.email_id)
    logger.info(f"Chat History: {chat_history}")
    ai = GeminiAI()
    ai.start_chat(chat_history)
    response = ai.send_message(chat_payload.chat_msg)
    logger.info(f"Response from AI: {response}")
    # Create a chat history onbject
    chat_response = [
        {"role": response[-2].role, "parts": [response[-2].parts[0].text]},
        {"role": response[-1].role, "parts": [response[-1].parts[0].text]}]
    chat_payload.chat_msg = chat_response
    chat_payload.chat_ts = datetime.datetime.now().isoformat()
    persisted_chat = ChatDao().create_chat(chat_payload)
    logger.info(f"Chat created: {persisted_chat}")
    return JSONResponse(persisted_chat)


@chat_router.get("/chat/{email_id}")
async def get_chats(email_id):
    """
    Get chat messages for the user

    Args:
        email_id (_type_): Email ID of the user

    Returns:
        _type_: _description_
    """
    logger.info(f"Fetching chats for user: {email_id}")
    return JSONResponse(ChatDao().get_chats_by_user(email_id))

@chat_router.delete("/chat")
async def delete_chats(delete_req: AIChatDeleteRequest):
    """
    Delete chat messages for the user

    Args:
        email_id (_type_): Email ID of the user

    Returns:
        _type_: _description_
    """
    logger.info(f"Deleting chats for user: {delete_req.email_id}")
    return JSONResponse(ChatDao().delete_chats_by_user(delete_req.email_id))
