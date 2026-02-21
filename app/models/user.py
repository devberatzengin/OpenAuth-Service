import uuid
import enum
from sqlalchemy import Column, String, Boolean, DateTime, Enum, func
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import Base

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):

    __tablename__ = "tblusers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    
    email = Column(String(255), unique=True, index=True, nullable=False)
    
    hashed_password = Column(String, nullable=True)
    
    phone_number = Column(String(20), nullable=True)
    role = Column(Enum(UserRole), default=UserRole.USER, nullable=False)
    is_active = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())