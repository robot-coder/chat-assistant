# FastAPI server for Chat Assistant
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user: str
    text: str

@app.get("/")
async def get():
    return HTMLResponse(open('index.html').read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")