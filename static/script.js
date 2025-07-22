async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    if (!message.trim()) return;

    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<div class='user-msg'>You: ${message}</div>`;
    input.value = "";

    const response = await fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });
    const data = await response.json();
    chatBox.innerHTML += `<div class='bot-msg'>AI: ${data.reply}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
}
