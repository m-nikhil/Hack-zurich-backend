## Developer Guide

- Database used: mongoDB
- mark todo things as 'TO-DO' (as is). Maintain same facilitates search.
- preferred mongoUI : mongoDB compass
- openapi is used for documentaion and input/output validation
- All the REST logic reside in api folder
- JWT is for Authentication
- authzApiRules - custom library to do Authorization
- Methodview.py has all the mongoDB related functions/logics
- to make the first admin, you need to add isAdmin: true (boolean) manually in the DB

## Installation Guide

### Python version:
- minimum 3.6 

### Setup: 
- pip3 install pipenv
- pipenv install

### To run:
- pipenv shell
- flask run

### Swagger
- hit endpoint /ui