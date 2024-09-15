import asyncio
from app.models.schemas import ChatRequest

# Handle logic
async def handle_chat(chat_request: ChatRequest):
    str_chunks = "This is a test string".split()
    for chunk in str_chunks:
        yield f"data: {chunk}\n"
        await asyncio.sleep(1)