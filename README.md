# OpenAuth-Service

OpenAuth-Service is a simple and scalable **authentication microservice** built with **FastAPI**.  
It is designed to be reusable, database-independent, and easy to integrate into modern backend systems.

---

## What is this project?

This project provides a **central authentication service** for applications.  
It focuses on clean structure, JWT-based authentication, and production-ready setup.

---

## Features

- JWT based authentication
- Refresh token support
- Clean and modular architecture
- Database independent (PostgreSQL, SQLite, etc.)
- FastAPI powered REST API
- Docker support
- Easy to extend and maintain

---

## Technologies

- Python 3.10+
- FastAPI
- SQLAlchemy
- PostgreSQL / SQLite
- Docker

---

## Getting Started

### Requirements

Make sure you have the following installed:

- Python 3.10 or higher
- Git
- Docker (optional)

---

## Installation

### Clone the repository

```bash
git clone https://github.com/devberatzengin/OpenAuth-Service.git
cd OpenAuth-Service
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

Update the values according to your environment.

---

## Run Locally

### Using virtual environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app.main:app --reload
```

The service will run on:

```
http://localhost:8000
```

---

## Run with Docker

```bash
docker build -t openauth-service .
docker run -p 8000:8000 openauth-service
```

or

```bash
docker compose up --build
```

---

## API Documentation

Swagger UI is available at:

```
http://localhost:8000/docs
```

You can test all endpoints from this page.

---

## Testing

To run tests:

```bash
pytest
```

---

## Project Structure

The project follows a clean and layered structure to keep the code readable and testable.

- API layer  
- Service layer  
- Database layer  
- Core configuration  

---

## Contributing

Contributions are welcome.

Steps:

1. Fork the repository  
2. Create a new branch  
3. Add your feature or fix  
4. Open a pull request  

---

## Contact

If you have questions or suggestions, feel free to open an issue.