from sqlalchemy.orm import Session
from app.models.user import User
from uuid import UUID

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    # Acceptance Criteria: get_by_id()
    def get_by_id(self, user_id: UUID):
        return self.db.query(User).filter(User.id == user_id).first()

    # Acceptance Criteria: get_by_email()
    def get_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    # Acceptance Criteria: create_user()
    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user