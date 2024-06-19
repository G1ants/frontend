from enum import StrEnum
from pydantic import BaseModel
from models.agent import Agent


class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"


class Message(BaseModel):
    role: Role
    content: str


class MessageRequest(BaseModel):
    message: str
    chat_history: list[Message]
    agent: Agent


class MessageResponse(BaseModel):
    content: str
    agent: Agent
