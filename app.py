from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'chair',
                'price': 15.99
            },
            {
                'name': 'desk',
                'price': 200
            }
        ]
    }
]


@app.get("/store")
def get_stores():
    return {'stores': stores}


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "store not found"}, 404


@app.get("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "store not found"}, 404


@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    if new_store["name"] not in [store["name"] for store in stores]:
        stores.append(new_store)
        return new_store, 201
    else:
        return {"message": "store already exists"}, 400


@app.post("/store/<string:name>/item")
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            if new_item["name"] not in [item["name"] for item in store["items"]]:
                store["items"].append(new_item)
                return new_item, 201
            else:
                return {"message": "item already exists"}, 400
    return {"message": "store not found"}, 404
