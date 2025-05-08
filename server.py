import fastapi
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user: str
    content: str

messages = []

@app.post("/send_message/")
async def send_message(message: Message):
    messages.append(message)
    # Here you would call your LLM and get a response
    response = "This is a response from the LLM."
    messages.append(Message(user="Assistant", content=response))
    return messages

@app.get("/messages/")
async def get_messages():
    return messages

@app.post("/upload_text/")
async def upload_text(file: UploadFile = File(...)):
    contents = await file.read()
    # Process the text file contents
    return {"filename": file.filename}

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    # Process the image file contents
    return {"filename": file.filename}
