#!/usr/bin/env python

from flask import Flask
from flask_restful import Api
import logging
import logging.config
from restcontroller.config.logconfig import logconfig

logging.config.dictConfig(logconfig)
logger = logging.getLogger(__name__)

fapp = Flask(__name__)
fapi = Api(fapp)

from restcontroller import apis
