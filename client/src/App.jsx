import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [answer, setAnswer] = useState("");

  const sendMessage = async () => {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message,
      }),
    });

    const data = await response.json();

    setAnswer(data.answer);
  };

  return (
    <div>
      <h1>AI RAG Assistant</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask something..."
      />

      <button onClick={sendMessage}>
        Send
      </button>

      <p>{answer}</p>
    </div>
  );
}

export default App;