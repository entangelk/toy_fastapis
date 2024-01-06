from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel, EmailStr

class toyteam(Document):
    question: Optional[str] = None
    options: Optional[list] = None
    answer: Optional[int] = None
    score: Optional[int] = None
  
    class toyteam_Settings:
        name = "toyteam"


class input_answer(Document):
    name:Optional[str] = None
    qustion1:Optional[str] = None
    qustion2:Optional[str] = None
    qustion3:Optional[str] = None
    qustion4:Optional[str] = None
    qustion5:Optional[str] = None

    class input_answer_Settings:
        name = 'input_answer'