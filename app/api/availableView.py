from flask import request
from app.MethodView import SuperView
import json
from bson import ObjectId


class AvailableView(SuperView): 
    """ Create needs service
    """
    method_decorators = []
    _decorators = []

    resource = 'available'
    mask = None

    def getAll(self):
      return self.retrieveAll()