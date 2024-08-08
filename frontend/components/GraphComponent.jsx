import React from "react";

function GraphComponent({ graphHtml }) {
  return <div dangerouslySetInnerHTML={{ __html: graphHtml }} />;
}

export default GraphComponent;
