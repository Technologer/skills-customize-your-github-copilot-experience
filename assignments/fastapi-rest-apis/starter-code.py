"""Starter code for Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Mergington Inventory API")


class ItemCreate(BaseModel):
    name: str
    category: str
    price: float


class Item(ItemCreate):
    id: int


# TODO: Use this in-memory store for CRUD operations.
items: dict[int, Item] = {}
next_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Mergington Inventory API"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/items", response_model=Item, status_code=201)
def create_item(payload: ItemCreate) -> Item:
    global next_id
    # TODO: Create an Item with a unique ID, save it in `items`, and return it.
    raise NotImplementedError


@app.get("/items", response_model=list[Item])
def list_items() -> list[Item]:
    # TODO: Return all stored items as a list.
    raise NotImplementedError


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    # TODO: Return the requested item or raise HTTPException(status_code=404).
    raise NotImplementedError


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, payload: ItemCreate) -> Item:
    # TODO: Update an existing item or raise HTTPException(status_code=404).
    raise NotImplementedError


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, str]:
    # TODO: Delete an existing item or raise HTTPException(status_code=404).
    raise NotImplementedError
