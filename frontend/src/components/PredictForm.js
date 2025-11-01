import React, { useState } from "react";

export default function PredictForm() {
  const [days, setDays] = useState(1);
  const [result, setResult] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ days_ahead: parseInt(days) }),
    });
    const data = await response.json();
    setResult(data.predicted_prices);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          value={days}
          onChange={(e) => setDays(e.target.value)}
          min="1"
          style={{ padding: "5px", marginRight: "10px" }}
        />
        <button type="submit" style={{ padding: "5px 10px" }}>
          Predict
        </button>
      </form>
      <div style={{ marginTop: "20px" }}>
        {result.length > 0 && (
          <div>
            <h3>Predicted Prices:</h3>
            <ul>
              {result.map((price, idx) => (
                <li key={idx}>{price.toFixed(2)}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </div>
  );
}
