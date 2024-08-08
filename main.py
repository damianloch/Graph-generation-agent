from fastapi import FastAPI
from agent.graph_agent import GraphAgent

app = FastAPI()
graph_agent = GraphAgent()

@app.post("/generate-graph/")
async def generate_graph(user_input: str):
    graph_code = graph_agent.handle_user_request(user_input)
    return {"graph_code": graph_code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
