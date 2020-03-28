from flask import request
from app.MethodView import SuperView
import json
from bson import ObjectId


class RequestView(SuperView): 
    """ Create request service
    """
    method_decorators = []
    _decorators = []

    resource = 'request'
    mask = {}

    def getAll(self):
      search = {}
      search['request.status'] = 'ongoing'
      return self.retrieveAll(search)