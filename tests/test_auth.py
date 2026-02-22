def test_register_user(client):
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123",
        "first_name": "Berat",  
        "last_name": "Zengin"   
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


import uuid 

def test_login_user(client):
    """Giriş yapıp token alabiliyor muyuz?"""
    unique_email = f"user_{uuid.uuid4().hex[:6]}@test.com"
    password = "securepassword123"
    
    client.post("/auth/register", json={
        "email": unique_email,
        "password": password,
        "first_name": "Berat",
        "last_name": "Zengin"
    })
    
    response = client.post(
        "/auth/login", 
        data={"username": unique_email, "password": password}
    )
    
    assert response.status_code == 200
    json_data = response.json()
    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"

def test_register_invalid_data(client):
    """Geçersiz veriyle custom error handler çalışıyor mu?"""
    response = client.post("/auth/register", json={"email": "not-an-email"})
    assert response.status_code == 422
    
    data = response.json()
    assert data["success"] is False 
    assert data["code"] == "VALIDATION_ERROR"