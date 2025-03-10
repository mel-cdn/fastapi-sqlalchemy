# FastAPI with SQLAlchemy

A FastAPI service using SQLAlchemy to interact with database MySQL database.

A simple approach how to implement Dependency Injection by switching database from PostgreSQL and "Mocked" DynamoDB.

---

## Requirements

1. Install [Python 3.12](https://www.python.org/)
2. Postgres service running
    - Create a database
    - Create a Clients table with the following columns:
        - Id: INTEGER PRIMARY KEY, IDENTITY
        - FirstName: VARCHAR
        - LastName: VARCHAR
    - Add at least 1 row to the table

## Getting Started

```bash

# Create and activate virtual environment
$ python -m venv venv
$ source venv/bin/activate
(venv)$ # Environment activated

# Install dependencies
$ pip install -r requirements.txt
```

Update `.env.local` with your database details.

## Scripts

```bash
# Start application locally
$ ./run-local-service
```

## Test Routes

```bash
# [GET] Retrieve clients transactions should be against PostgresSQL
$ curl -X GET http://127.0.0.1:9000/api/clients

[
  {"firstName":"Postgres", "lastName":"Ultimatum"}
]

# [POST] Create client transactions should be against DynamoDB (mocked)
$ curl -X POST http://127.0.0.1:9000/api/clients

{"firstName":"Maximo", "lastName":"Dynamo Jr."}
```
