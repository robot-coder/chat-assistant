# Chat Assistant Documentation

## Overview
This Chat Assistant is a simple implementation of a conversational AI interface, similar to ChatGPT. It consists of a front-end JavaScript interface and a back-end Python FastAPI server that integrates with LiteLLM to handle user queries.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/robot-coder/chat-assistant.git
   cd chat-assistant
   ```
2. Install the required dependencies:
   - For the front-end, ensure you have a web server to serve the `index.html` file.
   - For the back-end, create a virtual environment and install FastAPI and LiteLLM:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install fastapi uvicorn lite-llm
   ```

## Usage Examples
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your web browser and navigate to `http://localhost:8000` to access the Chat Assistant.
3. Enter your queries in the input field and press enter to send them to the assistant.

## API Reference
- **POST /ask**: Sends a user query to the LLM and returns the response.
  - **Request Body**:
    ```json
    {
      "message": "Your question here"
    }
    ```
  - **Response**:
    ```json
    {
      "response": "LLM's response here"
    }
    ```

## Architectural Overview
- **Front-end**: The front-end is built using HTML and JavaScript, providing a user-friendly interface for interaction.
- **Back-end**: The back-end is built with FastAPI, handling requests and integrating with LiteLLM to fetch responses from the selected LLM.

## Deployment
Once the application is ready, deploy it to Render.com following their deployment instructions. Make sure to include a link to your live site in the README of your repository.

## Extensions
- Allow for text file uploads to add to the prompt context.
- Allow for image file uploads to send to multimodal LLMs.
- Allow for side-by-side LLM response comparison of two models.

## License
This project is licensed under the MIT License.