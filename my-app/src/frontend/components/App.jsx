import React, { useState } from "react";
import InputComponent from "./InputComponent";
import GraphComponent from "./GraphComponent";
//import { Card } from "@/components/ui/card"; // Adjusted import
import { Card } from "../../components/ui/card";

function App() {
  const [graphHtml, setGraphHtml] = useState("");

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
      setGraphHtml(data.graph_code);
    } catch (error) {
      console.error("Error generating graph:", error);
      setGraphHtml("<p>Error generating graph. Please try again.</p>");
    }
  };

  return (
    <div className="p-4 space-y-4">
      {" "}
      {/* Apply padding and spacing classes */}
      <Card>
        <InputComponent onSubmit={handleInput} />
      </Card>
      <Card>
        <GraphComponent graphHtml={graphHtml} />
      </Card>
    </div>
  );
}

export default App;
