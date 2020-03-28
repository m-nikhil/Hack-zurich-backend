from flask import request
from app.MethodView import SuperView
import json
from bson import ObjectId


class NeedView(SuperView): 
    """ Create needs service
    """
    method_decorators = []
    _decorators = []

    resource = 'need'
    mask = {}

    def getAll(self):
      search = {}
      search['need.status'] = 'ongoing'
      return self.retrieveAll(search)