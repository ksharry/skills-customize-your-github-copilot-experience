from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(title="Books API - Starter")


class Book(BaseModel):
    id: Optional[int] = None
    title: str
    author: str
    year: Optional[int] = None


# simple in-memory "database"
books_db: List[Book] = []
_next_id = 1


def _get_next_id() -> int:
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid


@app.get("/books", response_model=List[Book])
def list_books():
    return books_db


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for b in books_db:
        if b.id == book_id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201, response_model=Book)
def create_book(book: Book):
    book.id = _get_next_id()
    books_db.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: Book):
    for i, b in enumerate(books_db):
        if b.id == book_id:
            book.id = book_id
            books_db[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    for i, b in enumerate(books_db):
        if b.id == book_id:
            books_db.pop(i)
            return
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-main:app", host="127.0.0.1", port=8000, reload=True)
