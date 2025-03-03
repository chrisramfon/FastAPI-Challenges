# FastAPI-Challenges

## Challenge-01

Create a simple FastAPI application with two endpoints:
1. `/users`: Returns a list of users (as JSON) from the `data.json` file.
2. `/users/{user_id}`: Returns the details of a specific user by their ID.

**Constraints:**

* Use Python and FastAPI as the primary technologies (no other libraries or frameworks allowed).
* The `data.json` file is provided below. Make sure you use it correctly in your solution.

**Challenge Goals:**

* Create a FastAPI application with the two endpoints described above.
* Use Python's `json` module to read data from the `data.json` file and return it as JSON in response to `/users`.
* Implement dependency injection using FastAPI's built-in features (e.g., `Depends`) to inject the user data into your endpoint functions.

## Challenge-02

**Challenge:**

Create a FastAPI application that implements the following endpoints:
1. `/books`: Returns all books in JSON format.
2. `/books/{book_id}`: Returns the book with the given `book_id` if it exists, or returns an error message otherwise.

The twist is that you need to use dependency injection to inject the list of books into your endpoint functions. The list of books should be read from a file named `books.json`.

**Constraints:**

* You can only modify the code provided below.
* Do not hardcode any data (e.g., book IDs, titles).
* Use FastAPI's built-in features for dependency injection and JSON handling.

**Starting Code:**
```python
from fastapi import FastAPI, Depends
import json

app = FastAPI()

def read_books_json() -> Annotated[str, Depends]:
    # TO DO: Read the books from a file named 'books.json'
    pass

@app.get("/books")
async def get_all_books(data: Annotated[str, Depends(read_books_json)]):
    # TO DO: Return all books in JSON format
    pass

@app.get("/books/{book_id}")
async def get_book(book_id: int, data: Annotated[str, Depends(read_books_json)]):
    # TO DO: Return the book with the given {book_id} if it exists, or return an error message otherwise
    pass
```
