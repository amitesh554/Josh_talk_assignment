# Task Management API

This project is a Django-based task management system that allows users to create tasks, assign them to other users, and retrieve tasks assigned to a specific user. The API is built using Django and Django REST Framework (DRF).

## Features

- Create new tasks
- Assign tasks to one or more users
- Retrieve tasks assigned to a specific user

## Prerequisites

- Python 3.x
- Django 3.x or higher
- Django REST Framework

## Setup Instructions

1. Clone the repository
    ```bash
    git clone <your-repository-url>
    cd task_manager
    ```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Migrate the database
    ```bash
    python manage.py migrate
    ```

4. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server
    ```bash
    python manage.py runserver
    ```
    The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Endpoints

### 1. Create a Task
- **URL**: `/api/tasks/`
- **Method**: POST

#### Request Body:
    ```json
    {
      "name": "New Task",
      "description": "Task description",
      "task_type": "feature"
    }
    ```

#### Sample Response:
    ```json
    {
      "id": 1,
      "name": "New Task",
      "description": "Task description",
      "created_at": "2024-10-22T10:00:00Z",
      "task_type": "feature",
      "completed_at": null,
      "status": "pending",
      "assigned_users": []
    }
    ```

### 2. Assign a Task to Users
- **URL**: `/api/tasks/<task_id>/assign/`
- **Method**: POST

#### Request Body:
    ```json
    {
      "user_ids": [1, 2]
    }
    ```

#### Sample Response:
    ```json
    {
      "id": 1,
      "name": "New Task",
      "description": "Task description",
      "created_at": "2024-10-22T10:00:00Z",
      "task_type": "feature",
      "completed_at": null,
      "status": "pending",
      "assigned_users": [
        {
          "id": 1,
          "username": "user1",
          "email": "user1@example.com"
        },
        {
          "id": 2,
          "username": "user2",
          "email": "user2@example.com"
        }
      ]
    }
    ```

### 3. Get Tasks for a User
- **URL**: `/api/users/<user_id>/tasks/`
- **Method**: GET

#### Sample Response:
    ```json
    [
      {
        "id": 1,
        "name": "New Task",
        "description": "Task description",
        "created_at": "2024-10-22T10:00:00Z",
        "task_type": "feature",
        "completed_at": null,
        "status": "pending",
        "assigned_users": [
          {
            "id": 1,
            "username": "user1",
            "email": "user1@example.com"
          }
        ]
      }
    ]
    ```


