from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
# 변경 후 코드
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # DATABASE_URL: Optional[str] = None
    DATABASE_URL : Optional[str] = None
      # async-await == 네크워크의 속도와 맞추기 위해 넣는 기능(방식은 비동기)
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(),
                          document_models=[User])
    class Config:
        env_file = ".env"