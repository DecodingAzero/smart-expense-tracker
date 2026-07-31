import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
    expenses,
    file,
    indent=4,
    ensure_ascii=False
)


def get_next_id(expenses):
    if not expenses:
        return 1
    return max(expense["id"] for expense in expenses) + 1