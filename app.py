from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import PipeLine1
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return "Hello, you!"


if __name__ == "__main__":
    app.run()

