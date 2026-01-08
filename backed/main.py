from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="AI Engine")

# Pydantic model for POST requests
class Prompt(BaseModel):
    input: str

# Root endpoint (GET) to check server status
@app.get("/")
def root():
    return {"status": "AI Engine running"}

# POST endpoint for AI inference (dummy response for now)
@app.post("/infer")
def infer(prompt: Prompt):
    # Replace this with real LLM later
    response_text = f"AI Response: You said -> {prompt.input}"
    return {"response": response_text}
