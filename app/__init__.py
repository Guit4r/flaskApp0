from flask import Flask
 
app = Flask(__name__, static_folder='static')
 
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '29a8a9e70366c8c25f39781653eaf21b607c236f1db2bae6'
app.config['JSON_AS_ASCII'] = False
 
from app import views  # noqa