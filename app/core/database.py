from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# MSSQL kullanıyorsan driver belirtmek gerekebilir
# PostgreSQL veya SQLite için standart devam eder
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# SQLite için thread güvenliği, diğerleri için boş sözlük
connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args=connect_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # Tüm modellerin atası

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()