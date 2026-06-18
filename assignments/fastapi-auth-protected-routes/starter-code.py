"""Starter code for FastAPI Authentication and Protected Routes assignment."""

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Mergington Auth API")


class LoginRequest(BaseModel):
    username: str
    password: str


class UserProfile(BaseModel):
    username: str
    role: str


# In-memory user data for practice only.
users = {
    "ava": {"password": "learn123", "role": "student", "token": "token-ava"},
    "sam": {"password": "admin123", "role": "admin", "token": "token-sam"},
}


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI Auth Assignment"}


@app.post("/login")
def login(payload: LoginRequest) -> dict[str, str]:
    # TODO: Validate username/password against `users`.
    # TODO: Return {"access_token": <token>} on success.
    # TODO: Raise HTTPException(status_code=401) for invalid credentials.
    raise NotImplementedError


def get_current_user(x_auth_token: str | None = Header(default=None)) -> dict:
    # TODO: Check that `x_auth_token` is provided and matches a user token.
    # TODO: Return a dict with authenticated user info (username + role).
    # TODO: Raise HTTPException(status_code=401) if token is missing/invalid.
    raise NotImplementedError


@app.get("/profile", response_model=UserProfile)
def profile(current_user: dict = Depends(get_current_user)) -> UserProfile:
    return UserProfile(username=current_user["username"], role=current_user["role"])


@app.get("/admin/reports")
def admin_reports(current_user: dict = Depends(get_current_user)) -> dict[str, str]:
    # TODO: Allow only admins.
    # TODO: Raise HTTPException(status_code=403) for authenticated non-admin users.
    # TODO: Return a simple report message for admin users.
    raise NotImplementedError
