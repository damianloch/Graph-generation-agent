import React, { useState } from "react";
import { Input } from "../../components/ui/input"; // Adjusted import
import { Button } from "../../components/ui/button"; // Adjusted import

function InputComponent({ onSubmit }) {
  const [input, setInput] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(input);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 p-4">
      <Input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter graph details..."
        className="w-full"
      />
      <Button type="submit" className="w-full">
        Generate Graph
      </Button>
    </form>
  );
}

export default InputComponent;
