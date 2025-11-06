# 🧩 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small, well-structured REST API using the FastAPI framework. You will design endpoints, validate input with Pydantic, and run the app with Uvicorn.

## ⏱️ Estimated time

- Approximate time to complete: 3–6 hours

## 🔢 Prerequisites

- Python 3.9 or newer installed
- Basic knowledge of Python (functions, data structures)
- Familiarity with HTTP concepts (GET/POST/PUT/DELETE)
- Starter files: `starter-main.py`, `requirements.txt` (included)

## 🎯 Learning outcomes

After completing this assignment students will be able to:

- Create FastAPI endpoints for CRUD operations
- Use Pydantic models for request validation and response models
- Run a FastAPI app with Uvicorn and test endpoints manually
- Write small unit tests for core functions (optional)

---

## 📝 Tasks

### 🛠️ Task 1 — Implement a Book CRUD API (Required)

#### Description

Implement a simple REST API to manage a collection of books. Each book should have an `id`, `title`, `author`, and optional `year`.

#### Requirements (Acceptance criteria)

Completed submission must satisfy ALL of the following:

- Provide endpoints:
  - `GET /books` — list all books
  - `GET /books/{book_id}` — get a single book by id
  - `POST /books` — create a new book (validate body)
  - `PUT /books/{book_id}` — update an existing book
  - `DELETE /books/{book_id}` — delete a book
- Use Pydantic models for request/response validation and type hints.
- Return appropriate HTTP status codes (201 on create, 404 when not found, 200 on success, 204 on delete, etc.).
- Store data in an in-memory structure (dictionary/list); persistence is optional for this assignment.
- Provide clear error messages for invalid input.

Example JSON for creating a book:

```
{
  "title": "The Little Prince",
  "author": "Antoine de Saint-Exupéry",
  "year": 1943
}
```

Points: 70

#### Hints

- Keep core logic (e.g., add_book, get_book, update_book) in separate functions to make testing easier.
- Use `from pydantic import BaseModel` to define input/output schemas.
- Run the app with Uvicorn during development: `uvicorn starter-main:app --reload`.

---

### 🛠️ Task 2 — Extras & Tests (Optional / Bonus)

#### Description

Add one or more optional features or provide unit tests for the API logic.

#### Suggested extras

- Add query parameters for filtering or pagination on `GET /books`.
- Add basic authentication (e.g., API key) for protected endpoints.
- Persist data to a simple JSON file.
- Write `pytest` tests for at least two core functions or endpoints.

Points (bonus): up to 10–20

#### Hints

- Use `TestClient` from `fastapi.testclient` (based on `requests`) for endpoint tests.
- Structure code so that the FastAPI `app` object is importable by test files.

---

## 📦 Deliverables (what to submit)

- `starter-main.py` (implementation of the API)
- `requirements.txt` listing dependencies (e.g., fastapi, uvicorn)
- `README.md` in the assignment folder (this file — include any additional notes you added)
- (Optional) `tests/` folder with pytest files

Include the following in your `README.md` (student submission README):

- How to run the app locally
- Any assumptions you made
- How to run tests (if included)

---

## ✅ Student checklist (before submitting)

- [ ] API endpoints work as specified and return correct status codes.
- [ ] I included a `README.md` with run instructions.
- [ ] I validated input with Pydantic models.
- [ ] (If requested) I included unit tests and they pass locally.

---

## 🧾 Grading rubric (suggested)

- Correctness & acceptance criteria: 70%
- Code quality, structure & documentation: 15%
- Tests & extras (if provided): 10%
- README & submission completeness: 5%

---

## 🛠️ Local testing & evaluation

Run the app locally:

```bash
python -m pip install -r requirements.txt
uvicorn starter-main:app --reload
```

Open `http://127.0.0.1:8000/docs` to see the interactive API docs (Swagger UI).

Run tests (if using pytest):

```bash
pytest -q
```

---

## 📚 Resources

- FastAPI docs: https://fastapi.tiangolo.com/
- Pydantic docs: https://pydantic-docs.helpmanual.io/
- Uvicorn docs: https://www.uvicorn.org/

---

## 📨 Submission instructions

Please submit a ZIP or push to the assigned branch with a short message containing:

- Assignment ID: `fastapi-rest-apis`
- Your name and student ID
- Files included and how to run

Good luck — implement clean APIs and test them!
