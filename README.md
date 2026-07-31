# Smart Expense Tracker API

## Overview

The Smart Expense Tracker API is a RESTful web service built using **FastAPI**. It allows users to manage personal expenses by creating, viewing, filtering, calculating totals, and deleting expense records.

Expense data is stored in a local JSON file, so no database setup is required.

## Features

* Add a new expense
* View all expenses
* Filter expenses by category
* Calculate total expenses
* Calculate total expenses for a specific category
* Delete an expense
* Automatic API documentation using Swagger UI

## Project Structure

```text
smart-expense-tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── pytest.ini
│
├── src/
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   ├── storage.py
│   ├── expenses.json
│   └── __init__.py
│
└── tests/
    └── test_api.py
```

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the Server

```bash
uvicorn src.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

Interactive API documentation is available at:

```
http://127.0.0.1:8000/docs
```

## Run the Tests

```bash
pytest
```

## API Endpoints

| Method | Endpoint                        | Description                          |
| ------ | ------------------------------- | ------------------------------------ |
| GET    | `/`                             | Welcome endpoint                     |
| POST   | `/expenses`                     | Add a new expense                    |
| GET    | `/expenses`                     | View all expenses                    |
| GET    | `/expenses?category=Food`       | Filter expenses by category          |
| GET    | `/expenses/total`               | Calculate total expenses             |
| GET    | `/expenses/total?category=Food` | Calculate total expenses by category |
| DELETE | `/expenses/{expense_id}`        | Delete an expense                    |

## Technologies Used

* Python
* FastAPI
* Pydantic
* Pytest
* Uvicorn

## Bonus Feature

* Automatic OpenAPI/Swagger documentation provided by FastAPI.
