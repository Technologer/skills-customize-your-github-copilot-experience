# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request and response models, and basic CRUD-style operations.

## 📝 Tasks

### 🛠️ Create Your First API Endpoints

#### Description
Set up a FastAPI app and implement a few foundational endpoints so you can verify your server is running correctly.

#### Requirements
Completed program should:

- Create a FastAPI application instance in `starter-code.py`.
- Implement a `GET /` endpoint that returns a welcome message.
- Implement a `GET /health` endpoint that returns a simple status value.
- Run successfully with Uvicorn.

### 🛠️ Add Request and Response Models

#### Description
Define Pydantic models and use them in API routes to validate incoming data and return consistent response objects.

#### Requirements
Completed program should:

- Create an `ItemCreate` model for incoming item data.
- Create an `Item` model for stored and returned data.
- Implement a `POST /items` endpoint that validates input and returns the created item.
- Return proper HTTP status codes for successful creation and missing resources.

### 🛠️ Implement Basic CRUD Operations

#### Description
Use an in-memory data store to support reading, updating, and deleting items by ID.

#### Requirements
Completed program should:

- Implement `GET /items` to list all items.
- Implement `GET /items/{item_id}` to retrieve one item.
- Implement `PUT /items/{item_id}` to update an existing item.
- Implement `DELETE /items/{item_id}` to remove an item.
- Return a clear `404` response when an item does not exist.