from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent.graph_agent import GraphAgent

# Define the request body structure
class GraphRequest(BaseModel):
    user_input: str

app = FastAPI()
graph_agent = GraphAgent()

@app.post("/generate-graph/")
async def generate_graph(request: GraphRequest):
    try:
        graph_code = graph_agent.handle_user_request(request.user_input)
        return {"graph_code": graph_code}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Graph Generation API. Use /generate-graph/ to create graphs."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
