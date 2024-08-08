import React, { useState } from "react";
import InputComponent from "./components/InputComponent";
import GraphComponent from "./components/GraphComponent";

function App() {
  const [graphHtml, setGraphHtml] = useState("");

  const handleInput = async (userInput) => {
    const response = await fetch("/generate-graph/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_input: userInput }),
    });
    const data = await response.json();
    setGraphHtml(data.graph_code);
  };

  return (
    <div>
      <InputComponent onSubmit={handleInput} />
      <GraphComponent graphHtml={graphHtml} />
    </div>
  );
}

export default App;
