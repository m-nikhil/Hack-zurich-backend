from flask import request
from app.MethodView import SuperView
import json


class ItemTagView(SuperView): 
    """ Create Item Tage service
    """
    method_decorators = []
    _decorators = []

    resource = 'itemtag'
    mask = {}
    
    #tag cannot be updated

    def post(self):
      body = request.json
      return self.insert(body)

    def delete(self, itemTagId):
      # though a tag is deleted, it lives in document where its foreign key
      return self.remove(itemTagId)

    def get(self, itemTagId):
      return self.retrieve(itemTagId)

    def getAll(self):
      return self.retrieveAll()