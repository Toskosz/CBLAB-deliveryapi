# CBLAB-deliveryapi

REST API para serviço de delivery. Desenvolvida utilizando o framework flask.

## Backlog
| O que | Porque |
| ------------------- | ------------------- |
| Integração de banco de dados NoSQL |  Persistência dos dados em caso de interrompimento da API |
| Testes Unitários |  Garantir funcionamento em caso de novas funcionalidades |
| Testes de Integração entre BD e Recursos | Garantir o funcionamento integrado dos componentes | 
| Automatização dos testes | Acelerar processo de desenvolvimento |

## Setup
### Pré requisitos
- git
- Docker

### Passos para execução
1 - Clonar repositório
```
git clone https://github.com/Toskosz/CBLAB-deliveryapi.git
```
2 - Com o docker instalado, subir o container com
```
cd CBLAB-deliveryapi
sudo make up
```
3 - Após subir o container para confirmar funcionamento da aplicação basta acessar http://localhost:5000/

4- Para acabar com o ambiente basta executar
```
sudo make down
```


## Funcionalidades
| Funcionalidade | Método |Endpoint |
| ------------------- | ------------------- | ------------------- |
| Criar novo pedido | POST |/pedidos |
| Consultar pedido | GET | /pedidos/\<int:id\> |
| Atualizar pedido | PUT | /pedidos/\<int:id\> | 
| Deletar pedido | DELETE | /pedididos/\<int:id\> |
| Consultar todos os pedidos | GET | /pedidos |
| Consultar estado e possíveis ações de pedido | GET | /pedidos/\<int:id\>/estado |
| Alterar estado de pedido | PUT | /pedidos/\<int:id\>/estado |
