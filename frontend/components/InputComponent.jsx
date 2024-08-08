import React, { useState } from "react";

function InputComponent({ onSubmit }) {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(input);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter graph details..."
      />
      <button type="submit">Generate Graph</button>
    </form>
  );
}

export default InputComponent;
