from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user_sh import UserCreate, UserOut, UserLogin, Token
from app.services.user_service import UserService
from app.core.security import create_access_token
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register",
            summary="Register New User",
            response_model=UserOut,
            status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.register_user(user_data)

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
):
    service = UserService(db)
    login_result = service.authenticate_user(form_data.username, form_data.password)
    
    if not login_result:
        raise HTTPException(status_code=401, detail="Wrong email or password")
    
    return login_result

@router.get("/me",
            summary="Get Current User Profile",
            response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user