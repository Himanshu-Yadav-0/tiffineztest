from pydantic import BaseModel
from uuid import UUID

class TiffinServiceCreate(BaseModel):
    name: str
    location: str
    description: str
    owner_id: UUID

class TiffinServiceOut(BaseModel):
    id: UUID
    name: str
    location: str
    description: str
    owner_id: UUID
    active: bool

    class Config:
        orm_mode = True
