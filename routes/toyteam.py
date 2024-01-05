from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

# 응시한 애들 값
@router.get("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})

@router.post("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})


# 문제 페이지
@router.get("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})

@router.post("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="positionings/forms.html", context={'request':request})
