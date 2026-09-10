from fastapi import APIRouter
from app.models.req_res_structure import ChatRequest
router = APIRouter(prefix ="/chat")

@router.get("/")
async def chat(request: ChatRequest):
    return "Bushra Nikhat"