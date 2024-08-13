import React, { useState } from "react";
import InputComponent from "./InputComponent";
import GraphComponent from "./GraphComponent";

function App() {
  const [graphCode, setGraphCode] = useState("");

  const handleInput = async (userInput) => {
    try {
      const response = await fetch("http://127.0.0.1:8000/generate-graph/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_input: userInput }),
      });

      if (!response.ok) {
        throw new Error("Failed to generate graph");
      }

      const data = await response.json();
      console.log("Received Graph Code:", data.graph_code);
      setGraphCode(data.graph_code);
    } catch (error) {
      console.error("Error generating graph:", error);
      setGraphCode("<p>Error generating graph. Please try again.</p>");
    }
  };

  return (
    <div>
      <InputComponent onSubmit={handleInput} />
      <GraphComponent graphCode={graphCode} />
    </div>
  );
}

export default App;
