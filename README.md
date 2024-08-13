
# Graph Generation AI Agent

This project implements an AI agent that generates Python code for creating graphs based on user input. The AI agent is integrated into a FastAPI application, and uses OpenAI's API to generate the code.

## Features

- Generates Python code to create graphs using Plotly.
- Logs the generated code for debugging and analysis.
- Supports cross-origin requests with CORS.
- Executes the generated code and returns the graph as HTML.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- LangChain
- OpenAI API Key
- dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/graph-generation-agent.git
   cd graph-generation-agent
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Start the FastAPI server, in the root:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the API via `http://127.0.0.1:8000`. Use the `/generate-graph/` endpoint to generate graphs.
```
{
    "user_input" : "Generate a graph of Canada's Population over the last 3 years"
}
```


4. The generated Python code will be logged to both the console and a file named `generated_code.log`.

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/generate-graph/" -H "Content-Type: application/json" -d "{"user_input":"Create a bar chart with X values ['A', 'B', 'C'] and Y values [10, 20, 30]."}"
```
