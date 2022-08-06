# CBLAB-deliveryapi

REST API desenvolvida utilizando o framework flask.

## Backlog
| Oque | Porque |
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
2 - Com o docker instalado
```
cd CBLAB-deliveryapi
sudo make up
```
3 - Após subir o container para confirmar funcionamento da aplicação basta acessar [http://localhost:5000/]
