from flask import abort, request, g
import logging
from http import HTTPStatus
from restcontroller import fapp
from restcontroller.lib.auth import verify_token, auth

logger = logging.getLogger(__name__)

@fapp.before_request
def before_request_func():
    # excluding auth api
    if not request.path.endswith('auth'):
        # HTTP Basic Auth
        if (request.authorization and auth(request.authorization['username'],
            request.authorization['password'])):
            g.user = request.authorization['username']
        # Payload Auth
        elif(request.json and 'username' in request.json and 'password' in request.json
                and auth(request.json['username'], request.json['password'])):
                g.user = request.json['username']
                # deleting user credentials for not to print in audit logs
                del request.json['username']
                del request.json['password']
        # Custom Token Auth - header key x-access-tokens
        else:
            verify_token()
