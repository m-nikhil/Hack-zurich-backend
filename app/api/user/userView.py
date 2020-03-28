from flask import request
from app.MethodView import SuperView
import json
from app.util import exists


class UserView(SuperView): 
    """ Create User service
    """
    method_decorators = []
    _decorators = []

    resource = 'user'
    mask = {'password', 'location.cityId' }

    def post(self):
      body = request.json
      # fetch city
      if exists(body,['location','cityId']):
        body['location']['city'] = self.retrieve(body['location']['cityId'],'city',['city'])[0]['city']
      return self.insert(body)

    def put(self, userId):
      body = request.json
      # fetch city
      if exists(body,['location','cityId']):
        body['location']['city'] = self.retrieve(body['location']['cityId'],'city',['city'])[0]['city']
      return self.update(userId, body)

    def delete(self, userId):
      return self.remove(userId)

    def get(self, userId):
      return self.retrieve(userId)

    def getAll(self):
      return self.retrieveAll()