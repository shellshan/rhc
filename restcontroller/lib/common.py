from flask import abort, request
import logging
from http import HTTPStatus
from restcontroller import fapp
from restcontroller.lib.auth import verify_token

logger = logging.getLogger(__name__)

@fapp.before_request
def before_request_func():
    if not request.path.endswith('auth'):
        verify_token()
