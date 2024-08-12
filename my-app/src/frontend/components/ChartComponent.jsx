import React, { useEffect, useState } from "react";
import axios from "axios";
import { Card, CardContent, Loader } from "@/components/ui/card"; // Adjust based on actual Shadcn components

const ChartComponent = ({ userInput }) => {
  const [graphCode, setGraphCode] = useState("");

  useEffect(() => {
    axios
      .post("http://127.0.0.1:8000/generate-graph/", { user_input: userInput })
      .then((response) => {
        setGraphCode(response.data.graph_code);
      })
      .catch((error) => {
        console.error("Error fetching graph code:", error);
      });
  }, [userInput]);

  return (
    <Card>
      <CardContent>
        {graphCode ? (
          <div dangerouslySetInnerHTML={{ __html: graphCode }} />
        ) : (
          <Loader />
        )}
      </CardContent>
    </Card>
  );
};

export default ChartComponent;
