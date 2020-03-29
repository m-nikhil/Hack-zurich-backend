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
    mask = None

    def getAll(self):
      return self.retrieveAll(search)