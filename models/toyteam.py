from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class User(Document):
    question: Optional[str] = None
    options: Optional[list] = None
    answer: Optional[str] = None
    score: Optional[str] = None
  
    class Settings:
        name = "toyteam"
  