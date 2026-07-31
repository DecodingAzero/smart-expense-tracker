from typing import Optional

from fastapi import APIRouter, HTTPException

from src.models import Expense
from src.storage import (
    load_expenses,
    save_expenses,
    get_next_id,
)

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API"
    }


@router.post("/expenses")
def add_expense(expense: Expense):

    expenses = load_expenses()

    new_expense = {
        "id": get_next_id(expenses),
        "title": expense.title,
        "amount": expense.amount,
        "category": expense.category,
        "date": expense.date.isoformat()
    }

    expenses.append(new_expense)

    save_expenses(expenses)

    return new_expense

from fastapi import status

@router.post(
    "/expenses",
    status_code=status.HTTP_201_CREATED
)

@router.get("/expenses")
def get_expenses(category: Optional[str] = None):

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    return expenses

@router.get("/expenses/total")
def get_total_expenses(category: Optional[str] = None):

    expenses = load_expenses()

    if category:
        expenses = [
            expense
            for expense in expenses
            if expense["category"].lower() == category.lower()
        ]

    total = sum(expense["amount"] for expense in expenses)

    return {
        "category": category,
        "total": total
    }


@router.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    expenses = load_expenses()

    expense_to_delete = next(
        (expense for expense in expenses if expense["id"] == expense_id),
        None
    )

    if expense_to_delete is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    expenses.remove(expense_to_delete)

    save_expenses(expenses)

    return {
        "message": "Expense deleted successfully"
    }