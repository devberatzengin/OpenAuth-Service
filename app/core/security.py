import hmac
import hashlib
import bcrypt
from app.core.config import settings

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
    peppered = _get_peppered_password(plain_password)
    return bcrypt.checkpw(peppered, hashed_password.encode('utf-8'))