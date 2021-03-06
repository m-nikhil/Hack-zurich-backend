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
    mask = None

    #TODO tags not checked with the backend

    def post(self,userId):
      body = request.json
      with self.transaction() as session:
        with session.start_transaction():
          self.insert_subdocument_array(userId,body,'user','needs', 'ALL', None)
          return self.insert(body)

    def delete(self,userId, needId):
      with self.transaction() as session:
        with session.start_transaction():
          self.remove_subdocument_array(userId, needId, 'user', 'needs')
          return self.remove(needId)

    def get(self, userId, needId):
      return self.retrieve(needId)

    def getAll(self,userId):
      return self.retrieveAll()