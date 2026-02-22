import pytest
from app.core.security import hash_password, verify_password

def test_password_hashing_success():
    password = "kanka_cok_gizli_sifre"
    hashed = hash_password(password)
    
    assert password != hashed

    assert verify_password(password, hashed) is True

def test_wrong_password_fails():
    password = "dogru_sifre"
    wrong_password = "yanlis_sifre"
    hashed = hash_password(password)
    
    assert verify_password(wrong_password, hashed) is False

def test_empty_password():
    password = ""
    hashed = hash_password(password)
    assert verify_password("", hashed) is True