from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Model for user input
class UserInput(BaseModel):
    prompt: str
    llm_choice: str

# Endpoint to handle chat messages
@app.post("/chat/")
async def chat(input: UserInput):
    # Here you would integrate LiteLLM to get a response from the selected LLM
    # For now, we will return a mock response
    response = f"You asked: {input.prompt} using {input.llm_choice}"
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)