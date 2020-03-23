from flask import request, abort
from http import HTTPStatus
from functools import wraps
from simplepam import authenticate
import jwt
import datetime
import logging

logger = logging.getLogger(__name__)

def verify_token(f):
   @wraps(f)
   def decorator(*args, **kwargs):

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

      return f(*args, **kwargs, username=data.get('username'))
   return decorator

def auth(username, password):
    auth = authenticate(username, password)
    if auth:
        token = jwt.encode({'username': username, 'exp' :
                            datetime.datetime.utcnow() +
                            datetime.timedelta(minutes=30),
                            'iat': datetime.datetime.utcnow()},
                            'mysecret')
        return {'token': token.decode('UTF-8')}
    else:
        abort(HTTPStatus.UNAUTHORIZED, description='Authendication Failed')
