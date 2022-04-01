#Discussed the homework problems with @BhagyeshRathi and @PranavPandey
from flask import Flask

myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY = 'That-is-the-key')
from app import routes
