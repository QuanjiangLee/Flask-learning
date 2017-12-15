from flask import Flask
app = Flask(__name__)    #app instance
from app import routes   #'app' module
from app import views
app.config.from_object('config') #app configuration file