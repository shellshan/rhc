from flask import abort, Response, request
import logging
import datetime
from http import HTTPStatus
from flask_restful import reqparse, Resource, fields, marshal
import subprocess
import shlex
from restcontroller.lib.auth import auth
from restcontroller.lib.audit import audit

resource_fields = {
        'token': fields.String,
        }

class Authenticator(Resource):
    name = 'auth'
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('username', type = str, required=True, location = 'json')
        self.reqparse.add_argument('password', type = str, required=True, location = 'json')
        super().__init__(*args, **kwargs)

    def post(self):
        args = self.reqparse.parse_args()
        audit_list = [datetime.datetime.now(), request.remote_addr,
                      Authenticator.name,
                      args.username]
        response = auth(args.username, args.password, jwt_token=True)
        audit(*audit_list , int(HTTPStatus.OK))
        return marshal(response, resource_fields), HTTPStatus.OK
