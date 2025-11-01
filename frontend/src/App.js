import React, { useState } from "react";
import "./styles.css";

function App() {
  const [product, setProduct] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!product) {
      setMessage("Please enter a product name.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ days_ahead: product }),
      });

      if (!response.ok) throw new Error("Server error");

      const data = await response.json();
      setMessage(`Predicted price: ${data.predicted_prices}`);
    } catch (error) {
      setMessage("Failed to fetch. Try again later.");
      console.error(error);
    }
  };

  return (
    <div className="container">
      <h1>Market Price Detection</h1>
      {message && <div className="message">{message}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter product name"
          value={product}
          onChange={(e) => setProduct(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;
