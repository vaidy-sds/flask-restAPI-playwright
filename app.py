from flask import Flask, request
from db import stores, items
import uuid
from flask_smorest import abort

app = Flask(__name__)


@app.post("/store")
def create_store():
    store_data = request.get_json()
    if "name" not in store_data:
        abort(400, message="Missing required fields")
    for store in stores.values():
        if store["name"] == store_data["name"]:
            abort(400, message="Store already exists")
    store_id = uuid.uuid4().hex
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")
def create_item():
    item_data = request.get_json()
    if (
            "price" not in item_data or
            "store_id" not in item_data or
            "name" not in item_data
    ):
        abort(400, message="Missing required fields")
    if item_data["store_id"] not in stores:
        abort(404, message="Store not found")

    for item in items.values():
        if (item["name"] == item_data["name"] and
                item["store_id"] == item_data["store_id"]):
            abort(400, message="Item already exists in store")

    item_id = uuid.uuid4().hex
    new_item = {**item_data, "id": item_id}
    items[item_id] = new_item
    return new_item, 201


# get all stores
@app.get("/store")
def get_stores():
    return {'stores': list(stores.values())}


# get a store by id
@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found")


# get all items
@app.get("/item")
def get_items():
    return {'items': list(items.values())}


# get all items in a store
@app.get("/store/<string:store_id>/item")
def get_items_in_store(store_id):
    try:
        return {"items": [item for item in items.values() if item["store_id"] == store_id]}
    except KeyError:
        abort(404, message="Store not found")


# get an item by id
@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        abort(404, message="Item not found")


# delete an item by id
@app.delete("/item/<string:item_id>")
def delete_item(item_id):
    try:
        del items[item_id]
        return {"message": "Item deleted"}
    except KeyError:
        abort(404, message="Item not found")
