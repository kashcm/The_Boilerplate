import logging.config

from os import getenv
from flask import Flask, Blueprint
from flask_cors import CORS

from myproject import settings
from myproject.api.restplus import api
from myproject.api.module.routes import ns as module_namespace

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)
app = Flask(__name__, instance_relative_config=True)


def configure_app(app):
    app.config['SERVER_NAME'] = settings.SERVER_ADDRESS
    app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(app):
    configure_app(app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(module_namespace)
    app.register_blueprint(blueprint)
    CORS(app, supports_credentials=True)


initialize_app(app)
log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(settings.SERVER_ADDRESS))

if __name__ == "__main__":
    app.run(debug=settings.FLASK_DEBUG)
