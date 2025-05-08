# Chat Assistant JavaScript
const messagesContainer = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value;
    if (userMessage) {
        addMessage('User', userMessage);
        userInput.value = '';
        sendMessageToServer(userMessage);
    }
});

function addMessage(sender, text) {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${text}`;
    messagesContainer.appendChild(messageElement);
}

async function sendMessageToServer(message) {
    const response = await fetch('/ws', {
        method: 'POST',
        body: JSON.stringify({ user: 'User', text: message })
    });
    const data = await response.json();
    addMessage('Assistant', data.text);
}