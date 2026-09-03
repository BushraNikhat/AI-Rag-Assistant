from fastapi import FastAPI, HTTPException, UploadFile, File
from pypdf import PdfReader
from io import BytesIO
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

@app.post("/document", response_model=dict)
async def updoad_file(file:UploadFile=File(...)):
    content=await file.read()
    pdf = PdfReader(BytesIO(content))
    # print(pdf)

    text=""

    for page in pdf.pages:
        page_text=page.extract_text()
        text +=text+page_text+"\n"
    # content= await file.read()
    print(text)
    return {"filename": text, "content": len(content)}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
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

        
        data =response.json()
        return {"answer": data["message"]["content"]}

    except httpx.time:
        raise HTTPException(status_code=504, detail="Request to the chat model timed out.")

    except httpx.HttpError:
        raise HTTPException(status_code=502, detail="Error occurred while communicating with the chat model.")

    except Exception:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred")