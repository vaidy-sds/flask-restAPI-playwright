from flask import Flask
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from flask_smorest import Api

app = Flask(__name__)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['TITLE'] = 'Stores REST API'
app.config['API_VERSION'] = 'v1'
app.config['OPENAPI_VERSION'] = '3.0.2'
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config['OPENAPI_SWAGGER_UI_PATH'] = '/swagger-ui'
app.config['OPENAPI_SWAGGER_UI_URL'] = 'https://cdn.jsdelivr.net/npm/swagger-ui-dist/'
app.config['API_TITLE'] = 'Stores REST API'

api = Api(app)
api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)
