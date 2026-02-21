import pytest
from app.core.security import hash_password, verify_password

def test_password_hashing_success():
    """Şifreleme ve doğrulama başarılı olmalı."""
    password = "kanka_cok_gizli_sifre"
    hashed = hash_password(password)
    
    # Kriter: Plain password != stored value
    assert password != hashed
    # Kriter: Hash verify returns True
    assert verify_password(password, hashed) is True

def test_wrong_password_fails():
    """Yanlış şifre girildiğinde doğrulama başarısız olmalı."""
    password = "dogru_sifre"
    wrong_password = "yanlis_sifre"
    hashed = hash_password(password)
    
    assert verify_password(wrong_password, hashed) is False

def test_empty_password():
    """Boş şifre gibi uç vakalar (edge cases) yönetilmeli."""
    password = ""
    hashed = hash_password(password)
    assert verify_password("", hashed) is True