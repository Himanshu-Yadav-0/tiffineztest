from sqlalchemy.orm import Session
from models.tiffin_service import TiffinService
from schemas.tiffin_service import TiffinServiceCreate
from uuid import uuid4

def create_service(db: Session, service_data: TiffinServiceCreate):
    service = TiffinService(
        id=uuid4(),
        name=service_data.name,
        location=service_data.location,
        description=service_data.description,
        owner_id=service_data.owner_id
    )
    db.add(service)
    db.commit()
    db.refresh(service)
    return service
