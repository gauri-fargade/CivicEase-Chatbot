document.addEventListener("DOMContentLoaded", () => {
    const chatbox = document.getElementById("chatbox");
    const input = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");

    // Initial bot greeting from Flask variable
    addBot(typeof DEFAULT_GREETING !== "undefined" ? DEFAULT_GREETING : "Hi there! 👋 How can I help you today?");

    sendBtn.addEventListener("click", sendMessage);
    input.addEventListener("keypress", (e) => {
        if (e.key === "Enter") sendMessage();
    });

    function sendMessage() {
        let msg = input.value.trim();
        if (msg === "") return;

        addUser(msg);
        input.value = "";

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: msg })
        })
        .then(res => res.json())
        .then(data => addBot(data.reply))
        .catch(() => addBot("⚠️ Server error, please try again."));
    }

    function addUser(text) {
        let div = document.createElement("div");
        div.className = "user-msg";
        div.innerText = text;
        chatbox.appendChild(div);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function addBot(text) {
        let div = document.createElement("div");
        div.className = "bot-msg";
        div.innerHTML = text;
        chatbox.appendChild(div);
        chatbox.scrollTop = chatbox.scrollHeight;
    }
});
