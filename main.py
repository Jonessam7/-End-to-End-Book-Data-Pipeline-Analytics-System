"""
main.py
FastAPI REST layer over BookDatabaseManager (Phase 3).
Pattern based on O1_hello.py / O3_uvicorn_host.py.
Run with: python main.py   (or) uvicorn main:app --reload
"""

from fastapi import FastAPI, HTTPException, Body
import uvicorn
from database import BookDatabaseManager

app = FastAPI(title="Books Capstone API")
db = BookDatabaseManager("books.db")


def row_to_dict(row):
    return {"id": row[0], "title": row[1], "price": row[2],
            "in_stock": row[3], "rating": row[4]}


@app.get("/books")
async def get_books():
    return [row_to_dict(r) for r in db.get_all_books()]


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    row = db.get_book_by_id(book_id)
    if not row:
        raise HTTPException(status_code=404, detail="Book not found")
    return row_to_dict(row)


@app.post("/books")
async def create_book(book: dict = Body()):
    new_id = db.insert_book(book["title"], book["price"], book["in_stock"], book["rating"])
    return row_to_dict(db.get_book_by_id(new_id))


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: dict = Body()):
    if not db.get_book_by_id(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    db.update_book(book_id, book.get("title"), book.get("price"),
                    book.get("in_stock"), book.get("rating"))
    return row_to_dict(db.get_book_by_id(book_id))


@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    if not db.get_book_by_id(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete_book(book_id)
    return {"detail": f"Book {book_id} deleted"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
