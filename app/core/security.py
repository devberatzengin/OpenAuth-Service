import hmac
import hashlib
import bcrypt
from app.core.config import settings

from datetime import datetime, timedelta, timezone
from jose import jwt
from app.core.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def _get_peppered_password(password: str) -> bytes:
    digest = hmac.new(
        settings.SECRET_KEY.encode(),
        password.encode(),
        hashlib.sha256
    ).digest()
    return digest

def hash_password(password: str) -> str:
    peppered = _get_peppered_password(password)
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(peppered, salt)
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        peppered = _get_peppered_password(plain_password)
        return bcrypt.checkpw(peppered, hashed_password.encode('utf-8'))
    except Exception:
        return False

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt