from pydantic import BaseModel


class ChatRequest(BaseModel):
    userMsg: str
