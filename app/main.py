from fastapi import FastAPI
from fastapi import status
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from datetime import datetime
from app.core.config import settings
from app.core.database import engine
from app.core.logger import logger


from app.api import auth_api

app = FastAPI()
app.include_router(auth_api.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.warning(f"Validation Error: {exc.errors()} - URL: {request.url}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "success": False,
            "message": "Data Validation Error",
            "detail": exc.errors(),
            "code": "VALIDATION_ERROR"
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Kritik Hata: {str(exc)} - URL: {request.url}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "success": False, 
            "message": "Unexpected Server Error",
            "detail": str(exc),
            "code": "INTERNAL_SERVER_ERROR"
        },
    )


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


def get_system_info():
    print(f"Bağlanılan Veritabanı: {settings.DATABASE_URL}")
    print(f"Secret Key Yüklendi: {settings.SECRET_KEY[:4]}***")





if __name__ == "__main__":
    get_system_info()

