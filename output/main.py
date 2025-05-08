from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Chat Assistant API</h1>"

@app.post("/api/chat")
async def chat(message: Message):
    # Here you would integrate LiteLLM to get a response
    response = f"You said: {message.message}"
    return {"response": response}
