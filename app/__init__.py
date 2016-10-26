from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
