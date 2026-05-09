from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from conversation import chat_agent

app = FastAPI(
    title="SHL Conversational Assessment Agent"
)


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]


@app.get("/health")
def health_check():

    return {
        "status": "ok"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    messages = [
        {
            "role": msg.role,
            "content": msg.content
        }
        for msg in request.messages
    ]

    response = chat_agent(messages)

    return response