# PRD: OpenAuth Service

## 1. Overview

OpenAuth Service is an independent, scalable, and open-source Authentication Microservice designed for modern applications.  
It operates via a RESTful API and is built to be suitable for both small projects and production-level systems.  

By default, it will be developed using **Python** and **FastAPI**.

---

## 2. Problem Statement

In modern projects, authentication systems are repeatedly rewritten from scratch. This leads to:

- Security vulnerabilities  
- Loss of development time  
- Inconsistent architectures  
- Repetitive code across projects  
- Failure to implement production-grade security standards  

Especially in small projects, unnecessarily heavy solutions (e.g., large authentication frameworks just for login functionality) are often used.  

In larger projects, there is frequently a lack of secure and scalable authentication infrastructure.

**OpenAuth Service aims to solve this problem.**

---

## 3. Goals

- Create a reusable, independent Auth Microservice  
- Serve web and mobile applications via RESTful API  
- Provide multi-database support (SQLite, PostgreSQL, MSSQL)  
- Ensure secure password hashing and JWT-based authentication  
- Establish an open-source and extensible architecture  
- Be easily deployable with Docker  
- Design an architecture ready for future features such as refresh tokens, email verification, and multi-tenant support  

---

## 4. Success Metrics

- 50+ GitHub stars within the first 30 days  
- 0 critical security vulnerabilities (based on OWASP basic checks)  
- API response time < 200ms (in local test environment)  
- 80%+ test coverage (in later phases)  
- Integration into at least 3 different projects  

---

## 5. User Personas

### 1. Indie Developer

A developer who wants to quickly integrate an authentication system into small projects.

### 2. Startup Backend Developer

A team member looking for an independent authentication service compatible with microservice architecture.

### 3. Mobile Developer

A mobile developer who either does not have their own backend or prefers to keep authentication separate.

### 4. Open Source Contributor

A backend developer who wants to contribute to the project.

---

## 6. User Stories (High-Level)

- As a developer, I want to use the registration endpoint to add new users to my system.  
- As a user, I want to log in using my email and password.  
- As a system, I want to generate a JWT for authenticated users.  
- As a backend service, I want to validate tokens in incoming requests.  
- As an admin, I want to authorize users based on their roles (future phase).  

---

## 7. Scope

### In Scope (MVP - Phase 1)

- RESTful API  
- Register endpoint  
- Login endpoint  
- JWT Access Token  
- Role field (USER, ADMIN)  
- Password hashing (bcrypt)  
- SQLite as default database  
- PostgreSQL & MSSQL support (via configuration)  
- Environment configuration (.env)  
- Dockerfile  
- Swagger documentation (FastAPI auto-generated)  

### Out of Scope (Not included in MVP)

- Refresh tokens  
- Email verification  
- OAuth (Google, GitHub, etc.)  
- Multi-tenant architecture  
- gRPC  
- SOAP/XML  
- Frontend interface  
- Rate limiting  
- Account lock mechanism  

---

## 8. Assumptions

- Users will connect via REST API.  
- The application will initially be single-tenant.  
- Token validation will be handled by the client or other services.  
- Database connection details will be provided via environment variables.  

---

## 9. Risks

- Incorrect security implementation may introduce serious vulnerabilities.  
- Improper JWT secret management may compromise the system.  
- Multi-database support may create migration complexity.  
- Maintaining sustainability in an open-source project may be challenging.  

---
