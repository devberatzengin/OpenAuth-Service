def test_register_user(client):
    """Yeni kullanıcı kaydı başarılı mı?"""
    response = client.post("/auth/register", json={
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User"
    })
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

def test_login_user(client):
    """Giriş yapıp token alabiliyor muyuz?"""
    # Önce kayıt ol
    client.post("/auth/register", json={"email": "login@test.com", "password": "securepassword"})
    
    # Login ol (Form data formatında!)
    response = client.post("/auth/login", data={"username": "login@test.com", "password": "securepassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_me_unauthorized(client):
    """Token olmadan profile girilemez olmalı"""
    response = client.get("/auth/me")
    assert response.status_code == 401