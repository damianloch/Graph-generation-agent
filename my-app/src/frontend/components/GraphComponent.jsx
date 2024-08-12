import React from "react";
//import { Card, CardContent } from "@/components/ui/card"; // Adjusted import
import { Card, CardContent } from "../../components/ui/card";
const GraphComponent = ({ graphHtml }) => {
  return (
    <Card>
      <CardContent>
        {graphHtml ? (
          <div dangerouslySetInnerHTML={{ __html: graphHtml }} />
        ) : (
          <p>No graph to display</p>
        )}
      </CardContent>
    </Card>
  );
};

export default GraphComponent;
