from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.schemas import ChatRequest
from app.services.chat import handle_chat

router = APIRouter()


@router.post('')
async def chat(chat_request: ChatRequest):
    stream = handle_chat(chat_request)
    return StreamingResponse(stream, media_type="application/x-ndjson")