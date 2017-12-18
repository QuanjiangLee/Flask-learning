from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)    #app instance
from app import routes   #'app' module
from app import views
app.config.from_object('config') #app configuration file
db = SQLAlchemy(app)

from app import views, models
