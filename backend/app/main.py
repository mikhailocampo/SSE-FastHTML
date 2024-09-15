from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.api import router as api_router
from app.api.routes.home import router as home_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
app.include_router(home_router)
# Add exception handler
# Add exception handler
# Add event handlers