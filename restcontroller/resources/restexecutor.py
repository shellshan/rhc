from flask import abort, Response, request, g
import logging
import datetime
from http import HTTPStatus
from flask_restful import reqparse, Resource, fields, marshal
import subprocess
import shlex
from restcontroller.lib.commandexecutor import execute
from restcontroller.lib.audit import audit

output_fields = {
        'returncode': fields.Integer,
        'stderr': fields.String,
        'stdout': fields.String,
        }

resource_fields = {
        'output': fields.Nested(output_fields, allow_null=True),
        'error': fields.String,
        }

class RestExecutor(Resource):
    name = 'execute'
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('cmd', type = str, required=True, location = 'json')
        self.reqparse.add_argument('cwd', type = str, location = 'json')
        self.reqparse.add_argument('timeout', type = int, default=60, location = 'json')
        super().__init__(*args, **kwargs)

    def post(self):
        args = self.reqparse.parse_args()
        audit_list = [datetime.datetime.now(), request.remote_addr, g.user,
                      RestExecutor.name, request.json]
        try:
            response = execute(args.cmd, args.cwd, args.timeout, g.user)
        except Exception as e:
            audit(*audit_list, int(HTTPStatus.INTERNAL_SERVER_ERROR), e)
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, description=str(e))
        audit(*audit_list, int(HTTPStatus.OK), response)
        return marshal(response, resource_fields), HTTPStatus.OK
