from fastapi import FastAPI
from pydantic import BaseModel

from llm import generate_text
from router import classify_task
from memory import store_memory, get_memory

app = FastAPI()

class Request(BaseModel):
    input: str

@app.post("/infer")
def infer(req: Request):
    task = classify_task(req.input)

    if task != "TEXT":
        return {"response": f"{task} not supported yet."}

    store_memory(req.input)
    context = "\n".join(get_memory())

    prompt = f"""
Context:
{context}

User: {req.input}
Assistant:
"""
    response = generate_text(prompt)
    return {"response": response}