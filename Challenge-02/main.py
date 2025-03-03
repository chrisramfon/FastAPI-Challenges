from fastapi import FastAPI, Depends
from typing import Annotated
import json, os

app = FastAPI()

def read_books_json() -> Annotated[str, Depends]:
    try:
        file = open( 'books.json' )
        yield file.read()
    finally:
        file.close()

@app.get("/books")
async def get_all_books(data: Annotated[str, Depends(read_books_json)]):
    # TO DO: Return all books in JSON format
    return json.loads( data )

@app.get("/books/{book_id}")
async def get_book(book_id: int, data: Annotated[str, Depends(read_books_json)]):
    # TO DO: Return the book with the given {book_id} if it exists, or return an error message otherwise
    for book in json.loads( data ):
        if book[ 'id' ] == book_id: return book