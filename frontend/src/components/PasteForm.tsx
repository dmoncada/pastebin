import { useState } from "react";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function PasteForm() {
  const [content, setContent] = useState("");
  const [expiresIn, setExpiresIn] = useState(3600);
  const [pasteId, setPasteId] = useState<string | null>(null);

  const submitPaste = async () => {
    try {
      const res = await axios.post(`${API_URL}/paste`, {
        content,
        expires_in_seconds: expiresIn,
      });
      setPasteId(res.data.id);
    } catch (err) {
      console.error("Failed to create paste:", err);
    }
  };

  return (
    <div>
      <h2>Create a Paste</h2>
      <textarea
        rows={10}
        cols={50}
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <br />
      <label>Expires in seconds:</label>
      <input
        type="number"
        value={expiresIn}
        onChange={(e) => setExpiresIn(Number(e.target.value))}
      />
      <br />
      <button onClick={submitPaste}>Submit</button>
      {pasteId && (
        <p>
          Paste created:{" "}
          <a href={`/${pasteId}`}>
            {window.location.origin}/{pasteId}
          </a>
        </p>
      )}
    </div>
  );
}
