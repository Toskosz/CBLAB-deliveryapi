from flask import request
from flask_restplus import Resource, fields
from server.instance import *
from db import database
from maquina_estados import possiveis_estados
from datetime import datetime

pedidos_ns = server.pedidos_ns

item = pedidos_ns.model('Pedido', 
    {
    'cliente': fields.String(''),
    'produto': fields.String(''),
    'valor': fields.Float(0.0),
    }
)

estado = pedidos_ns.model('EstadoPedido',
    {
        'estado': fields.String('')
    }
)

class Pedido(Resource):
    def get(self, id):
        dados = database.query_by_id(id)
        if dados:
            return dados
        return {"message":"ITEM_NAO_ENCONTRADO"}, 404

    def delete(self, id):
        if database.delete_by_id(id):
            return '', 204
        return {"message":"ITEM_NAO_ENCONTRADO"}, 404

    @pedidos_ns.expect(item)
    def put(self, id):
        dados = database.query_by_id(id)
        novos_dados = request.get_json()

        if dados:
            dados["cliente"] = novos_dados["cliente"]
            dados["produto"] = novos_dados["produto"]
            dados["valor"] = novos_dados["valor"]
        else:
            return {"message":"ITEM_NAO_ENCONTRADO"}, 404 

        database.update_by_id(id, dados)
        return dados, 200

class ListaPedidos(Resource):

    def get(self):
        return database.query_all(), 200

    @pedidos_ns.expect(item)
    def post(self):
        novo_pedido = request.get_json()
        novo_pedido['entregue'] = False
        novo_pedido['estado'] = "RECEIVED"
        novo_pedido['timestamp'] = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        if database.insert_new(novo_pedido):
            return novo_pedido, 201
        else:
            return {"message":"ERRO_INESPERADO"}, 500

class EstadosPedido(Resource):
    
    def get(self, id):
        pedido = database.query_by_id(id)
        response = {}

        response['id'] = pedido['id']
        response['estado'] = pedido['estado']
        if pedido['estado'] == 'CANCELED' or pedido['estado'] == 'DELIVERED':
            response['operations'] = []
        else :
            response['operations'] = [{"method":"PUT","expects": {"estado": possiveis_estados[pedido['estado']]}}]
        
        return response

    @pedidos_ns.expect(estado)
    def put(self, id):
        novo_estado = request.get_json()
        dados_pedido = database.query_by_id(id)
        
        if dados_pedido['estado'] == 'CANCELED' or dados_pedido['estado'] == 'DELIVERED':
            return {"message":"ESTADO_INESPERADO"}, 400

        dados_pedido['estado'] = novo_estado['estado']

        database.update_by_id(id, dados_pedido)
        return dados_pedido, 200
