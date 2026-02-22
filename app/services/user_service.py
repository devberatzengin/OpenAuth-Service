from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.schemas.user_sh import UserCreate, UserLogin
from app.models.user import User
from app.core.logger import logger
from app.core.security import hash_password, verify_password, create_access_token
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
        
        logger.info(f"New User Succesfully Registered: {new_user.email}")

        return self.user_repo.create(new_user)

    def authenticate_user(self, email: str, password: str):

        user = self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            return None
        
        access_token = create_access_token(data={"sub": str(user.id)})
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
    
    def authenticate_user_by_form(self, email: str, password: str):
        user = self.user_repo.get_by_email(email) 
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user