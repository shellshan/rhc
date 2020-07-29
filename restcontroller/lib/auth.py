from flask import request, abort, g
from http import HTTPStatus
from functools import wraps
import pam
import jwt
import datetime
import logging

logger = logging.getLogger(__name__)

def verify_token():
    token = None
    if 'x-access-tokens' in request.headers:
       token = request.headers['x-access-tokens']

    if not token:
       abort(HTTPStatus.UNAUTHORIZED, description='Require Authentication')

    try:
       data = jwt.decode(token, 'mysecret')
    except jwt.exceptions.ExpiredSignatureError:
       abort(HTTPStatus.UNAUTHORIZED, description='Token Expired')
    except:
       abort(HTTPStatus.UNAUTHORIZED, description='Token Validation Failed')

    g.user = data.get('username')

def verify_token_dec(f):
   @wraps(f)
   def decorator(*args, **kwargs):
       verify_token()
       return f(*args, **kwargs)
   return decorator

def auth(username, password):
    pam_obj = pam.pam()
    auth = pam_obj.authenticate(username, password)
    if auth:
        token = jwt.encode({'username': username, 'exp' :
                            datetime.datetime.utcnow() +
                            datetime.timedelta(minutes=30),
                            'iat': datetime.datetime.utcnow()},
                            'mysecret')
        return {'token': token.decode('UTF-8')}
    else:
        abort(HTTPStatus.UNAUTHORIZED, description='{} {}'.format(pam_obj.code, pam_obj.reason))
