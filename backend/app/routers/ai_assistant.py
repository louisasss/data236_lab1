from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session

from app.database import get_db

router = APIRouter()


class ChatMessage(BaseModel):
    role: str   # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    message: str
    conversation_history: Optional[List[ChatMessage]] = []


class ChatResponse(BaseModel):
    reply: str
    recommendations: Optional[list] = []


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    # TODO: inject current_user (optional — works without auth too)
    # TODO: load user preferences from DB (if authenticated)
    # TODO: use LangChain to interpret payload.message + payload.conversation_history
    # TODO: extract filters: cuisine, price_range, dietary, occasion, ambiance
    # TODO: query restaurant DB with extracted filters
    # TODO: optionally use Tavily for web-search context
    # TODO: rank and return top recommendations as structured ChatResponse
    raise NotImplementedError
