from flask import Flask

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'chair',
                'price': 15.99
            }
        ]
    }
]


# get stores
@app.get("/stores")
def get_stores():
    return {"stores": stores}