from restcontroller import fapi
from restcontroller.resources import RestExecutor 

fapi.add_resource(RestExecutor, '/api/v1/execute', endpoint='execute')
