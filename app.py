from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:welcome123@127.0.0.1:3306/Venom'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'twqfygdhugejfdskvmdf'


from extensions import *
from controllers import *
from model import *

if __name__ == '__main__':
    app.init__app(db)
    app.init__app(migrate)
    app.run(port = 5000, debug = True)