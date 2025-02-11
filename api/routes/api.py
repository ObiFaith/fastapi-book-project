from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def root():
    return JSONResponse(content={"message": "Welcome to the API"})