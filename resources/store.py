import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from db import stores

blp = Blueprint('store', __name__, description='Operations on stores')


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}
        except KeyError:
            abort(404, message="Store not found")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {'stores': list(stores.values())}

    def post(self):
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
