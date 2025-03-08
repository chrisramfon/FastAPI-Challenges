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

# Challenge 03


**Challenge:**

You are building an API for a library management system. The system has the following features:
- Each book has a unique ID, title, author, and publication year.
- Users can search books by their titles or authors.

Your task is to create two endpoints in your FastAPI application:
1.  `/books`: This endpoint should return all available books as JSON data.
2.  `/search?q=<query>`: This endpoint should allow users to search for books based on either the title or author of a book. The query parameter will contain the user's search term.

**Requirements:**

- Both endpoints must be implemented using FastAPI and its dependencies (e.g., `json`).
- In the `/books` endpoint, you need to read JSON data from a file named `books.json`. This file contains all available books in the following format:
```json
[
    {
        "id": 1,
        "title": "Book A",
        "author": "Author A",
        "year": 2020
    },
    {
        "id": 2,
        "title": "Book B",
        "author": "Author B",
        "year": 2019
    }
]
```
- In the `/search?q=<query>` endpoint, you need to implement a search function that finds books based on either their titles or authors. The query parameter will contain the user's search term.
- If no book matches the given query, return an error message with HTTP status code 404 (Not Found).
- You can use any Python libraries and modules as needed.

**Example Output:**

When a user requests `/books`, your API should return all available books in JSON format:
```json
[
    {
        "id": 1,
        "title": "Book A",
        "author": "Author A",
        "year": 2020
    },
    {
        "id": 2,
        "title": "Book B",
        "author": "Author B",
        "year": 2019
    }
]
```
When a user requests `/search?q=<query>`, your API should return all books that match the given query. For example, if the query is `A`, your API might return:
```json
[
    {
        "id": 1,
        "title": "Book A",
        "author": "Author A",
        "year": 2020
    }
]
```


**Your Task:**

Write a FastAPI application that meets these requirements. You can use any Python libraries and modules as needed.

Let's start with a simple algorithm question. I'll give you the problem, and then we can go through it together.

# Challenge 04

**Problem:** Reverse Linked List

Given a singly linked list, write an algorithm to reverse the order of its nodes.

For example, if the input is:

1 -> 2 -> 3 -> 4 -> 5
The output should be:
5 -> 4 -> 3 -> 2 -> 1

**Constraints:**

* You can only use a single pointer (or variable) to keep track of the current node.
* You cannot create any new nodes or modify existing ones other than reversing their order.

# Challenge 05

Write a function `reverse_string(s)` that takes a string as input and returns the reversed string. For example, if the input is `"hello"`, the output should be `"olleh"`.

# Challenge 06

**Exercise 2: Find the First Duplicate**

Write a function `find_first_duplicate(arr)` that takes an array of integers as input and returns the first duplicate element in the array. If no duplicates are found, return -1 (or any other value you prefer).

For example:
```python
arr = [1, 2, 3, 4, 5]
print(find_first_duplicate(arr))  # Output: None (-1)

arr = [1, 2, 3, 4, 2]  # Duplicate found!
print(find_first_duplicate(arr))  # Output: 2
```

# Challenge 07

**Practice Problem 2:**

Write a function that takes two lists of integers as input and returns `True` if one list is a subset of another, and `False` otherwise. A subset means that all elements in the first list are present in the second list, possibly with duplicates.

For example:

* `[1, 2]` is a subset of `[1, 2, 3, 4]`
* `[1, 2, 3]` is not a subset of `[1, 2, 3, 4]`

