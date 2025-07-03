import React, { useState } from "react";

export default function App() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/process_query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: query, user_id: "student1" }),
    });
    const data = await res.json();
    setResponse(data.response);
    speak(data.response);
  };

  const speak = (text) => {
    const synth = window.speechSynthesis;
    const utter = new SpeechSynthesisUtterance(text);
    synth.speak(utter);
  };

  const handleMic = () => {
    const recognition = new window.webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();
    recognition.onresult = (event) => {
      setQuery(event.results[0][0].transcript);
    };
  };

  return (
    <div>
      <h1>Professor AI LMS Assistant</h1>
      <form onSubmit={handleSubmit}>
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask me anything..."
        />
        <button type="submit">Ask</button>
        <button type="button" onClick={handleMic}>🎤 Speak</button>
      </form>
      <p>{response}</p>
    </div>
  );
}
