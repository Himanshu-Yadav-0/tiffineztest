from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.tiffin_service import TiffinServiceCreate, TiffinServiceOut
from crud.tiffin_service import create_service

router = APIRouter(prefix="/services", tags=["Tiffin Services"])

@router.post("/", response_model=TiffinServiceOut)
def add_tiffin_service(service: TiffinServiceCreate, db: Session = Depends(get_db)):
    return create_service(db, service)
