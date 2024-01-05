from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from database.connections import Database
from models.toyteam import question,answer
from beanie import PydanticObjectId

router = APIRouter()

templates = Jinja2Templates(directory="templates/")

collection_toyteam = Database(question)
collection_input_answer = Database(answer)


# 응시한 애들 값
@router.get("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/data_list.html", context={'request':request})

@router.post("/data_list", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    return templates.TemplateResponse(name="toyteam/data_list.html", context={'request':request})


# 문제 페이지
@router.get("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    dict(request._query_params)
    
    question_list = await collection_toyteam.get_all()
    return templates.TemplateResponse(name="toyteam/exam_test.html", context={'request':request,'questions' : question_list})

@router.post("/exam_test", response_class=HTMLResponse) # 펑션 호출 방식
async def forms(request:Request):
    form_data = await request.form()
    question_dict = dict(form_data)

    # question_list = question(**question_dict)
    # await collection_user.save(user)

    question_list = await collection_toyteam.get_all()
    return templates.TemplateResponse(name="toyteam/exam_test.html", context={'request':request,'form_data':question_list})
