from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from fastapi.templating import Jinja2Templates
from config import VARIABLES

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/system", response_class=HTMLResponse)
async def system_page(request: Request):
    return templates.TemplateResponse("system.html", {"request": request})

@router.get("/api/system")
async def get_system():
    try:
        from main import get_opcua_client
        opcua_client = get_opcua_client()
        
        result = {}
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))