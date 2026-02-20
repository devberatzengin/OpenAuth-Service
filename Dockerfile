# 1. Base image olarak Python 3.12 kullanıyoruz
FROM python:3.12-slim

# 2. Çalışma dizinini belirliyoruz
WORKDIR /app

# 3. Sistem bağımlılıklarını kuruyoruz (psycopg2 gibi kütüphaneler için gerekebilir)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 4. Gereksinimleri kopyalayıp kuruyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Tüm proje dosyalarını kopyalıyoruz
COPY . .

# 6. Uygulamanın çalışacağı portu belirtiyoruz
EXPOSE 8000

# 7. Uygulamayı başlatıyoruz
# 0.0.0.0 önemli, yoksa Docker dışından erişemezsin
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]