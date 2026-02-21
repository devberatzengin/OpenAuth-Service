from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user_sh import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def register_user(self, user_data: UserCreate) -> User:
        db_user = self.user_repo.get_by_email(user_data.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This email is allready exists."
            )

        hashed_pwd = hash_password(user_data.password)

        new_user = User(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            hashed_password=hashed_pwd
        )

        return self.user_repo.create(new_user)

    def authenticate_user(self, login_data: UserLogin):

        user = self.user_repo.get_by_email(login_data.email)
        if not user:
            return None
        
        if not verify_password(login_data.password, user.hashed_password):
            return None
            
        return user