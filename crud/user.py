from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from uuid import uuid4

def create_user(db: Session, user_data: UserCreate):
    new_user = User(
        id=uuid4(),
        name=user_data.name,
        phone=user_data.phone,
        user_type=user_data.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
