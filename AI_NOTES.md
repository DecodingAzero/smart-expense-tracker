# AI_NOTES.md

## AI Usage Summary

This project was developed with the assistance of ChatGPT as a learning and development aid. AI was used to explain backend development concepts, suggest implementation approaches, and review code during development.

## How AI Assisted

AI was used for:

* Explaining REST API concepts and HTTP methods.
* Understanding the FastAPI framework and project structure.
* Creating Pydantic models for request validation.
* Implementing CRUD API endpoints.
* Designing a simple JSON-based storage layer.
* Writing and understanding automated tests using Pytest.
* Explaining Python syntax, FastAPI decorators, and best practices.
* Reviewing the overall project organization and documentation.

## My Contributions

I personally:

* Set up the development environment and project structure.
* Implemented and ran the application locally.
* Tested each API endpoint using Swagger UI and Pytest.
* Fixed project configuration issues, including the `src` import problem during testing.
* Verified that all endpoints worked correctly.
* Generated the required project files and organized the repository.
* Reviewed the generated code and documentation to understand how each component works.

## Verification Process

Instead of copying code directly, I verified the implementation by:

* Running the application after each major change.
* Executing the test suite using `pytest`.
* Testing API requests through the FastAPI Swagger interface.
* Checking that expense data was correctly stored in the JSON file.
* Debugging and resolving errors encountered during development.

## Design Decisions

The following implementation choices were made:

* FastAPI was selected because it provides automatic request validation and API documentation.
* A local JSON file was used for persistence since the assignment did not require a database.
* The project was organized into separate modules (`main.py`, `routes.py`, `models.py`, and `storage.py`) to improve readability and maintainability.
* Automated tests were included to verify the core API functionality.

## Reflection

Working with AI helped me understand backend development concepts more quickly, but I ensured that each part of the implementation was understood, tested, and validated before considering the project complete.
