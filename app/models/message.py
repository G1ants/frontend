from enum import StrEnum
from typing import Optional
from pydantic import BaseModel
from models.agent import Agent


class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    role: Role
    content: str
    is_rag: Optional[bool] = None


class MessageRequest(BaseModel):
    message: str
    chat_history: list[Message]
    agent: Agent


class MessageResponse(BaseModel):
    content: str
    agent: Agent
    is_rag: bool
