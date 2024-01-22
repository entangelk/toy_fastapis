from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import User
from models.toyteam import input_answer,toyteam
from models.events import Event
import json


from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings
from utils.paginations import Paginations

class Settings(BaseSettings):
    # DATABASE_URL: Optional[str] = None
    DATABASE_URL : Optional[str] = None
      # async-await == 네크워크의 속도와 맞추기 위해 넣는 기능(방식은 비동기)
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User, input_answer,toyteam,Event])
        
    class Config:
        env_file = ".env"

class Database:
    # model 즉 collection
    def __init__(self, model) -> None:
        self.model = model
        pass
        # 전체 리스트
    async def get_all(self):
        documents = await self.model.find_all().to_list()
        pass
        return documents
    # 상세 보기
    async def get(self, id:PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    # 저장
    async def save(self, document) -> None:
        doc = await document.create()
        return doc
    # 삭제
    async def delete(self, id: PydanticObjectId):
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
    
    # update with params json
    async def update_withjson(self, id: PydanticObjectId, body: json):
        doc_id = id

        # des_body = {k: v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {**body}}

        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc


    async def getsbyconditions(self, conditions:dict) -> [Any]:
        documents = await self.model.find(conditions).to_list()  # find({})
        if documents:
            return documents
        return False    

    async def getsbyconditionswithpagination(self
                                            , conditions:dict, page_number) -> [Any]:
    # find({})
        total = await self.model.find(conditions).count()
        pagination = Paginations(total_records=total, current_page=page_number)
        documents = await self.model.find(conditions).skip(pagination.start_record_number).limit(pagination.records_per_page).to_list()
        if documents:
            return documents, pagination
        return False    