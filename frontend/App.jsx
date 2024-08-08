import React, { useState } from "react";
import InputComponent from "./components/InputComponent";
import GraphComponent from "./components/GraphComponent";

function App() {
  const [graphHtml, setGraphHtml] = useState("");

  const handleInput = async (userInput) => {
    try {
      const response = await fetch("/generate-graph/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: userInput }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate graph");
      }

      const data = await response.json();
      setGraphHtml(data.graph_code);
    } catch (error) {
      console.error("Error generating graph:", error);
      setGraphHtml("<p>Error generating graph. Please try again.</p>");
    }
  };

  return (
    <div>
      <InputComponent onSubmit={handleInput} />
      <GraphComponent graphHtml={graphHtml} />
    </div>
  );
}

export default App;
