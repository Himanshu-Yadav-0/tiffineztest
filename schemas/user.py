from pydantic import BaseModel
from enum import Enum
from uuid import UUID
from datetime import datetime

class UserType(str, Enum):
    CUSTOMER = "CUSTOMER"
    OWNER = "OWNER"
    ADMIN = "ADMIN"
    DELIVERY = "DELIVERY"

class UserCreate(BaseModel):
    name: str
    phone: str
    user_type: UserType

class UserOut(BaseModel):
    id: UUID
    name: str
    phone: str
    user_type: UserType
    created_at: datetime

    class Config:
        orm_mode = True
