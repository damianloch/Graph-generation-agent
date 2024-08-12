from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from agent.graph_agent import GraphAgent
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now, you can specify specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the request body structure
class GraphRequest(BaseModel):
    user_input: str


graph_agent = GraphAgent()

@app.post("/generate-graph/")
async def generate_graph(request: GraphRequest):
    try:
        graph_code = graph_agent.handle_user_request(request.user_input)
        return JSONResponse(content={"graph_code": graph_code}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def root():
    return {"message": "Welcome to the Graph Generation API. Use /generate-graph/ to create graphs."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
