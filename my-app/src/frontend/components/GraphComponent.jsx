import React, { useEffect, useState } from "react";
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";
import {
  Card,
  CardHeader,
  CardContent,
  CardTitle,
} from "../../components/ui/card";

const GraphComponent = ({ graphCode }) => {
  const [graphData, setGraphData] = useState(null);

  useEffect(() => {
    if (graphCode) {
      console.log("Received Graph Code:", graphCode);
      try {
        const data = {
          labels: ["A", "B", "C"],
          datasets: [
            {
              label: "Bar Chart",
              data: [10, 20, 30],
              backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f"],
            },
          ],
        };

        const options = {
          responsive: true,
          plugins: {
            legend: {
              position: "top",
            },
            title: {
              display: true,
              text: "Bar Chart Example",
            },
          },
        };

        setGraphData({ data, options });
      } catch (error) {
        console.error("Error executing graph code:", error);
        setGraphData(null);
      }
    }
  }, [graphCode]);

  return (
    <Card>
      <CardHeader>
        <CardTitle>Generated Chart</CardTitle>
      </CardHeader>
      <CardContent>
        {graphData ? (
          <BarChart width={600} height={300} data={graphData.datasets[0].data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="value" fill="#8884d8" />
          </BarChart>
        ) : (
          <p>No graph to display. Please enter a valid prompt.</p>
        )}
      </CardContent>
    </Card>
  );
};

export default GraphComponent;
