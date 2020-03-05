import os

from flask import Flask
#from flask.Flask.  sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy                                                                                                                                                                                                                                                                                                                                                                                                                                    
from flask_sqlalchemy import SQLAlchemy
 


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "test.db"))

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
 
from inicio.catalog.views import catalog
app.register_blueprint(catalog)
 
db.create_all()