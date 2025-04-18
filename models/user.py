from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from datetime import datetime
from db.database import Base  # ✅ use absolute import now


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True, nullable=False)
    user_type = Column(Enum("CUSTOMER", "OWNER", "DELIVERY", "ADMIN", name="user_type_enum"))
    created_at = Column(DateTime, default=datetime.utcnow)
