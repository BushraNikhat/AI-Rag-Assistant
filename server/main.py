from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import httpx;

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
http_client = httpx.AsyncClient(
    timeout=120.0
)

class ChatRequest(BaseModel):
    message:str

class ChatResponse(BaseModel):
    answer:str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await http_client.post("http://localhost:11434/api/chat",
    json={
        "model":"llama3.2",
        "messages":[
            {
                "role":"user",
                "content":request.message
            }
        ],
        "stream":False
    })

    print("response:", response)
    data =response.json()
    return {"answer": data["message"]["content"]}