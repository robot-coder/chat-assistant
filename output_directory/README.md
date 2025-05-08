# Chat Assistant Documentation

## Overview
This Chat Assistant is a web application that allows users to interact with a language model through a chat interface. It is built using a FastAPI backend and a JavaScript frontend, providing a seamless experience similar to ChatGPT.

## Features
- **User Interface**: A clean and intuitive chat interface that displays the conversation history.
- **Continuous Conversation**: Users can maintain a continuous conversation with the language model.
- **LLM Selection**: Users can choose from different language models to interact with.
- **File Uploads**: Support for text and image file uploads to enhance the conversation context.
- **Side-by-Side Comparison**: Compare responses from different language models.

## Installation Instructions
1. **Clone the Repository**: Clone the repository from GitHub.
   ```bash
   git clone https://github.com/robot-coder/chat-assistant.git
   cd chat-assistant
   ```
2. **Set Up the Backend**:
   - Navigate to the backend directory and install the required dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
   - Run the FastAPI server:
   ```bash
   uvicorn server:app --reload
   ```
3. **Set Up the Frontend**:
   - Navigate to the frontend directory and open `index.html` in a web browser.

## Usage
- Open the web application in your browser.
- Select a language model from the dropdown menu.
- Start typing your messages in the chat input box.
- Upload files if needed to provide context.
- View responses from the language model in the chat window.

## Deployment
- Deploy the application on Render.com for public access. Follow the instructions on Render's website for deployment steps.

## License
This project is licensed under the MIT License.