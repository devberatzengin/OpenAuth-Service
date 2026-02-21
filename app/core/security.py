import hmac
import hashlib
from passlib.context import CryptContext
from app.core.config import settings 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def _get_peppered_password(password: str) -> str:
    return hmac.new(
        settings.SECRET_KEY.encode(), 
        password.encode(), 
        hashlib.sha256
    ).hexdigest()

def hash_password(password: str) -> str:
    return pwd_context.hash(_get_peppered_password(password))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(_get_peppered_password(plain_password), hashed_password)