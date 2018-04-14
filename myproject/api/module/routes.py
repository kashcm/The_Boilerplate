# encoding: utf-8
#ROUTES
import json
import logging
import http.client

from myproject.api.restplus import api
from flask_restplus import Namespace, Resource, fields

from myproject.api.module.services import definition

log = logging.getLogger(__name__)

ns = Namespace('myproject', description='module description')


@ns.route('/cluster_info')
@api.response(http.client.OK, 'Success')
@api.response(http.client.INTERNAL_SERVER_ERROR, 'Server processing Error')
class Example(Resource):
    def get(self):
        response = definition()
        return response



