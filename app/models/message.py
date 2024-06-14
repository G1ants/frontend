from enum import StrEnum
from pydantic import BaseModel

class Role(StrEnum):
    USER = "user"
    ASSISTANT = "assistant"
    
class Message(BaseModel):
    role: Role
    content: str
    
class MessageRequest(BaseModel):
    message: str
    chat_history: list[Message]

class MessageResponse(BaseModel): 
    message: str