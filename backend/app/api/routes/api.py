from fastapi import APIRouter
from app.api.routes import chat


router = APIRouter()

router.include_router(chat.router, prefix='/chat', tags=['chat'])