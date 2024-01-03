from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 회원 가입 form    /users/form
@router.get("/form", response_class=HTMLResponse) # 펑션 호출 방식
async def insert(request:Request):
    return templates.TemplateResponse(name="users/inserts.html", context={'request':request})

# 회원 가입 /users/insert -> users/login.html
@router.get("/insert", response_class=HTMLResponse) # 펑션 호출 방식
async def insert(request:Request):
    return templates.TemplateResponse(name="users/login.html", context={'request':request})
