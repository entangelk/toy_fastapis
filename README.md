```
~$ pip install fastapi uvicorn jinja2
~$ pip install python-multipart
~$ pip install beanie
~$ pip install pydantic
~$ pip install pydantic-settings
~$ pip install pydantic[email]
```

### [업무분장]
|멤버|역할|
|--|--|
|박요한|db 연결 세팅, 문제 풀기, 응시 결과|
|김유진|문제리스트|

### [파일 경로]
|파일속성|파일|설명|서버경로|
|--|--|--|--|
|python|[models/toyteam.py](models/toyteam.py)|DB 연결 모델||
|python|[routes/toyteam.py](routes/toyteam.py)|html 연결라우터||
|html|[question_list.html](templates/toyteam/question_list.html)|문제 리스트|/toy/question_list|
|html|[exam_test.html](templates/toyteam/exam_test.html)|문제 풀기|/toy/exam_test|
|html|[data_list.html](templates/toyteam/data_list.html)|응시 결과|/toy/data_list|