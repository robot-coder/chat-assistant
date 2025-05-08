# Chat Assistant Documentation

## Overview
This Chat Assistant project is designed to provide a conversational interface using FastAPI and a JavaScript frontend. The assistant leverages LiteLLM to interact with various language models (LLMs).

## Features
- **User Interface**: A responsive JavaScript frontend that mimics the ChatGPT interface.
- **Backend**: A Python FastAPI server that handles requests and responses between the user and the LLM.
- **Continuous Conversation**: Maintains context by storing messages in an array.
- **LLM Selection**: Users can choose from different LLMs.
- **File Uploads**: Supports text and image file uploads to enhance context.
- **Response Comparison**: Allows side-by-side comparison of responses from different models.

## Installation Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/robot-coder/chat-assistant.git
   cd chat-assistant
   ```
2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Backend**:
   ```bash
   uvicorn backend:app --reload
   ```
4. **Open the Frontend**: Open `frontend.html` in your web browser.

## Usage Instructions
- Enter your message in the input box and press enter to send.
- The assistant will respond based on the selected LLM.
- You can upload files to provide additional context.

## Deployment
The Chat Assistant is deployed on Render.com. You can access it at the link provided in the README.

## License
This project is licensed under the MIT License.