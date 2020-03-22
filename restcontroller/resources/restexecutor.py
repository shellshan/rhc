from flask import abort, Response, request
import logging
import datetime
from http import HTTPStatus
from flask_restful import reqparse, Resource, fields, marshal 
import subprocess
import shlex
from restcontroller.utils.commandexecutor import execute 
from restcontroller.utils.audit import audit

output_fields = {
        'returncode': fields.Integer,
        'stderr': fields.String,
        'stdout': fields.String,
        }

resource_fields = {
        'cmd': fields.String,
        'cwd': fields.String,
        'output': fields.Nested(output_fields, allow_null=True),
        'error': fields.String,
        }

class RestExecutor(Resource):
    def __init__(self, *args, **kwargs):
        self.logger = logging.getLogger(__name__)
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('cmd', type = str, required=True, location = 'json')
        self.reqparse.add_argument('cwd', type = str, required=True, location = 'json')
        self.reqparse.add_argument('timeout', type = int, default=60, location = 'json')
        super().__init__(*args, **kwargs)

    def post(self):
        args = self.reqparse.parse_args()
        audit_list = [datetime.datetime.now(), request.remote_addr, args.cmd, args.cwd]
        response = { 'cmd' : args.cmd, 'cwd': args.cwd }
        out = execute(args.cmd, args.cwd, args.timeout) 
        response.update(out)
        audit_list.append(response.get('error') or response.get('output'))
        audit(audit_list)
        return marshal(response, resource_fields), 200
