from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
