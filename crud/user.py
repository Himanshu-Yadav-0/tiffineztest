from utils.auth import hash_password
from models.user import User
from schemas.user import UserCreate
from sqlalchemy.orm import Session
from uuid import uuid4
from utils.auth import verify_password, create_token
from fastapi import HTTPException

def create_user(db: Session, data: UserCreate):
    new_user = User(
        id=uuid4(),
        name=data.name,
        phone=data.phone,
        password_hash=hash_password(data.password),  # ✅ hashed
        user_type=data.user_type
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, phone: str, password: str):
    user = db.query(User).filter(User.phone == phone).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # ✅ create JWT with user ID and type
    token = create_token({"sub": str(user.id), "role": user.user_type})
    return {"access_token": token, "token_type": "bearer"}

