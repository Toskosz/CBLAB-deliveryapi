import json


class BD():
    def __init__(self) -> None:
        self.bd = self.initialize_data()
        

    def initialize_data(self):
        with open('pedidos.json', 'r+') as json_file:
            bd = json.load(json_file)
        return bd

    def query_by_id(self, id):
        for pedido in self.bd["pedidos"]:
            try:
                if pedido["id"] == id:
                    return pedido
            except:
                continue
        return None

    def update_by_id(self, id, dados):
        for i in range(len(self.bd["pedidos"])):
            try:
                if self.bd["pedidos"][i]["id"] == id:
                    self.bd["pedidos"][i] = dados
            except:
                continue

    def delete_by_id(self, id):
        for i in range(len(self.bd["pedidos"])):
            try:
                if self.bd["pedidos"][i]["id"] == id:
                    self.bd["pedidos"].pop(i)

                    return True
            except:
                continue
        return False

    def query_all(self, ):
        return self.bd["pedidos"]

    def insert_new(self, dados):
        self.bd['pedidos'].append({'id':self.bd['nextId']}.update(dados))
        self.bd['nextId'] = self.bd['nextId'] + 1
        return True

database = BD()