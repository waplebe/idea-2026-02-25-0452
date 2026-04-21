# Simple Task Manager API

**Description:**

This project provides a simple RESTful API for managing tasks. It includes a backend API built with FastAPI and a basic frontend for creating, reading, updating, and deleting tasks.  It's designed to be a minimal, functional example of a full-stack web service.

**Why it's useful:**

This project demonstrates a basic workflow for building a web service, including API design, data storage, and a simple user interface. It's a good starting point for learning about REST APIs, database interaction, and frontend development.

**Installation & Setup:**

1.  **Clone the repository:**
    ```bash
    git clone https://github/your-username/simple-task-manager.git
    cd simple-task-manager
    ```

2.  **Set up the backend:**
    *   Create a `.env` file in the root directory and populate it with the following (replace with your actual values):
        ```
        DATABASE_URL=sqlite:///tasks.db
        ```
    *   Run the backend server:
        ```bash
        uvicorn app:app --reload
        ```

3.  **Set up the frontend:**
    *   Navigate to the `frontend` directory:
        ```bash
        cd frontend
        ```
    *   Run the frontend development server:
        ```bash
        npm start
        ```
        or
        ```bash
        python -m http.server 8000
        ```

4.  **Access the frontend:** Open your web browser and go to `http://localhost:8000`.

**API Endpoints:**

*   `GET /tasks`: Retrieves all tasks.
*   `POST /tasks`: Creates a new task.  Request body should be a JSON object with `title` and `description` fields.
*   `GET /tasks/{id}`: Retrieves a specific task by ID.
*   `PUT /tasks/{id}`: Updates a specific task by ID. Request body should be a JSON object with `title` and/or `description` fields.
*   `DELETE /tasks/{id}`: Deletes a specific task by ID.

**Example Usage:**

*   **Create a task:**
    `POST /tasks`
    Request Body:
    ```json
    {
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```
    Response:
    ```json
    {
      "id": 1,
      "title": "Grocery Shopping",
      "description": "Buy milk, eggs, and bread"
    }
    ```

*   **Get all tasks:**
    `GET /tasks`
    Response:
    ```json
    [
      {
        "id": 1,
        "title": "Grocery Shopping",
        "description": "Buy milk, eggs, and bread"
      }
    ]
    ```

**Dependencies:**

*   FastAPI
*   uvicorn
*   SQLAlchemy
*   Pydantic
*   frontend dependencies (listed in `package.json`)

**License:**

MIT License