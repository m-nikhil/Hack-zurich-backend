from flask import request
from app.MethodView import SuperView
import json
from bson import ObjectId


class UserNeedView(SuperView): 
    """ Create request service
    """
    method_decorators = []
    _decorators = []

    resource = 'need'
    mask = {'fromId' : False, 'toId' : False}

    #TODO tags not checked with the backend

    def post(self,userId):
      body = request.json
      with self.transaction() as session:
        with session.start_transaction():
          self.insert_subdocument_array(userId,body,'user','needs', 'ALL', None)
          return self.insert(body)

    def delete(self,userId, requestId):
      with self.transaction() as session:
        with session.start_transaction():
          self.remove_subdocument_array(userId, requestId, 'user', 'needs')
          return self.remove(requestId)

    def get(self, userId, requestId):
      return self.retrieve(requestId)

    def getAll(self,userId):
      return self.retrieveAll()