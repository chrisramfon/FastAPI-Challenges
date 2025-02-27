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
