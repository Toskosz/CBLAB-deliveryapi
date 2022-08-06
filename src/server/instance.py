from flask import Flask, Blueprint
from flask_restplus import Api


class Server():
    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.app,
            version="1.0",
            title="delivery_api")
        
        self.pedidos_ns = self.pedidos_ns()
        
        super().__init__()

    def pedidos_ns(self):
        return self.api.namespace(name='Pedidos', description='CRUD de pedidos', path='/')

    def run(self):
        self.app.run(
            port=5000,
            debug=True,
            host='0.0.0.0')

server = Server()