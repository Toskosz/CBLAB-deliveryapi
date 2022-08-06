from server.instance import server
from recursos.pedidos import Pedido, ListaPedidos, EstadosPedido
api = server.api
app = server.app

api.add_resource(Pedido, "/pedidos/<int:id>")
api.add_resource(ListaPedidos, "/pedidos")
api.add_resource(EstadosPedido, "/pedidos/<int:id>/estado")

if __name__ == '__main__':
    server.run()