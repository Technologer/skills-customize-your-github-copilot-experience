# 📘 Assignment: FastAPI Authentication and Protected Routes

## 🎯 Objective

Build on your FastAPI CRUD skills by adding simple token-based authentication and protected routes to control who can access API resources.

## 📝 Tasks

### 🛠️ Create a Login Endpoint

#### Description
Implement a login route that checks credentials and returns a token students can use in protected requests.

#### Requirements
Completed program should:

- Define a `LoginRequest` model with `username` and `password` fields.
- Implement `POST /login` to validate credentials from an in-memory user list.
- Return a token value when login is successful.
- Return a clear `401` error for invalid credentials.

### 🛠️ Protect API Routes with Dependencies

#### Description
Use FastAPI dependencies to validate tokens on incoming requests before accessing protected endpoints.

#### Requirements
Completed program should:

- Implement a dependency function that reads an auth token from request headers.
- Reject missing or invalid tokens with `401` responses.
- Use the dependency on `GET /profile` and return data for the authenticated user.
- Keep error messages consistent and easy to understand.

### 🛠️ Add Role-Based Access Control

#### Description
Extend authentication by allowing only admin users to access sensitive routes.

#### Requirements
Completed program should:

- Store user roles (for example: `student`, `admin`) in the in-memory user data.
- Protect `GET /admin/reports` so only admin users can access it.
- Return `403` for authenticated users without admin permission.
- Demonstrate the difference between `401` (not authenticated) and `403` (not authorized).