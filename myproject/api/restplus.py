import logging
import traceback

from flask_restplus import Api
from myproject import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='myproject', description='description')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    log.error(e)

    if not settings.DEBUG:
        log.error(message)
        return {'message': message}, 500
