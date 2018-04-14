
import os
import logging.config

logging.config.fileConfig('logging.conf')
log = logging.getLogger(__name__)
# Flask settings
FLASK_SERVER_NAME = os.getenv('SERVER_NAME') if os.getenv(
    'SERVER_NAME') else 'localhost'
FLASK_PORT = os.getenv('PORT') if os.getenv('PORT') else 5555
SERVER_ADDRESS = FLASK_SERVER_NAME + ':' + str(FLASK_PORT)
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

