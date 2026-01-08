from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Engine")

class Prompt(BaseModel):
    input: str

@app.get("/")
def root():
    return {"status": "AI Engine running"}

@app.post("/infer")
def infer(prompt: Prompt):
    return {"response": f"AI Response to: {prompt.input}"}
