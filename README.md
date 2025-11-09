# Assignment 10: Assignment-Secure User Model, Pydantic Validation, Database Testing, and Docker Deployment

![GitHub Actions CI/CD](https://github.com/am3696-dev/Assignment10/actions/workflows/main.yml/badge.svg)

This project is a secure REST API built with FastAPI as part of a course assignment. It implements a complete user model with secure password hashing, data validation using Pydantic, and a full CI/CD pipeline that automatically tests, scans, and deploys the application to Docker Hub.

---

## CI/CD & Deployment Information

This project is automatically built, tested, scanned, and deployed using GitHub Actions.

### Docker Hub Repository Link

The latest stable build of this application is available on Docker Hub at the following link:

**[https://hub.docker.com/r/am3696-dev/Assignment10](https://hub.docker.com/r/am3696-dev/Assignment10)**

---

## How to Run Locally

### 1. Prerequisites
* Python 3.10+
* Docker (for running Postgres) or a local PostgreSQL server

### 2. Setup
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/am3696-dev/Assignment10.git](https://github.com/am3696-dev/Assignment10.git)
    cd Assignment10
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Environment Variables:**
    Create a `.env` file in the root of the project and add your database credentials:
    ```.env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=mysecretpassword
    POSTGRES_DB=assignment10
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

### 3. Run the Application
```bash
uvicorn main:app --reload
```

---
### How to Run Tests Locally
To run the full test suite locally, ensure your environment is set up and your test database is accessible, then run:
```bash
pytest
```
