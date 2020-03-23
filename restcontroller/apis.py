from restcontroller import fapi
from restcontroller.resources import RestExecutor, Authenticator

fapi.add_resource(RestExecutor, '/api/v1/execute', endpoint='execute')
fapi.add_resource(Authenticator, '/api/v1/auth', endpoint='auth')
