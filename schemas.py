from pydantic import BaseModel
from enum import Enum


class Priority(str,Enum):
    high = "high"
    middle = "middle"
    low = "low"

class Title(BaseModel):
    title_content: str
    priority: Priority