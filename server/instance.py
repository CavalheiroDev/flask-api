from logging import debug
from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
        self.api = Api(self.blueprint, doc='/doc',
                       title='Sample Flask-SQLAlchemy')
        self.app.register_blueprint(self.blueprint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
        self.app.config['PROPAGATE_EXPECTIONS'] = True
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        def run(self, ):
            self.app.run(
                port=5000,
                debug=True,
                host='0.0.0.0'
            )
