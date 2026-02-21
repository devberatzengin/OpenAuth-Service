from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from datetime import datetime
from app.core.config import settings
from app.core.database import engine


from app.api import auth_api

app = FastAPI()
app.include_router(auth_api.router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "openauth-service",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.on_event("startup")
def startup_event():
    try:
        connection = engine.connect()
        print("✅ DB bağlantısı başarılı! Database Layer hazır.")
        connection.close()
    except Exception as e:
        print(f"❌ DB bağlantı hatası: {e}")


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print(f"Hata oluştu: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"message": "Sunucu tarafında bir hata oluştu.", "detail": str(exc)},
    )


def get_system_info():
    print(f"Bağlanılan Veritabanı: {settings.DATABASE_URL}")
    print(f"Secret Key Yüklendi: {settings.SECRET_KEY[:4]}***")





if __name__ == "__main__":
    get_system_info()

