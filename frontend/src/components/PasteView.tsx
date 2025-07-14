import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function PasteView() {
  const { id } = useParams<{ id: string }>();
  const [content, setContent] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    axios
      .get(`${API_URL}/paste/${id}`)
      .then((res) => setContent(res.data.content))
      .catch((err) => setError("Paste not found or expired"));
  }, [id]);

  return (
    <div>
      <h2>Paste Content</h2>
      {error ? <p>{error}</p> : <pre>{content}</pre>}
    </div>
  );
}
