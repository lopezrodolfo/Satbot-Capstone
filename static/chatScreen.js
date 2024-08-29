const chatContainer = document.getElementById("chat-container");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addUserMessage(userMessage) {
  const messageContainer = document.createElement("div");
  messageContainer.classList.add("user-message-container");

  const message = document.createElement("div");
  message.classList.add("message", "user-message");
  message.textContent = userMessage;

  messageContainer.appendChild(message);
  chatContainer.appendChild(messageContainer);

  input.value = "";
  input.focus();
}

function addBotMessage(botMessage) {
  const messageContainer = document.createElement("div");
  messageContainer.classList.add("message-container");

  const message = document.createElement("div");
  message.classList.add("message", "bot-message");
  message.textContent = botMessage;

  messageContainer.appendChild(message);
  chatContainer.appendChild(messageContainer);

  chatContainer.scrollTop = chatContainer.scrollHeight;
}

sendBtn.addEventListener("click", async () => {
  const userMessage = input.value.trim();
  if (!userMessage) return;

  addUserMessage(userMessage);

  const response = await fetch("/get_response", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: userMessage }),
  });

  const botMessage = await response.text();
  addBotMessage(botMessage);
});

input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    sendBtn.click();
  }
});
