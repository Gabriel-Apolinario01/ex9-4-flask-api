# Exercício 9.4 - API RESTful Flask na Azure

Este projeto foi desenvolvido para a disciplina de Engenharia de Software utilizando Flask, Azure App Services e GitHub Actions.

## Tecnologias utilizadas

- Python
- Flask
- Gunicorn
- Azure App Services
- GitHub Actions
- Postman

## Funcionalidades da API

### GET /

Retorna uma mensagem indicando que a API está funcionando.

### GET /usuarios

Retorna uma lista de usuários.

### GET /usuario/{id}

Retorna um usuário pelo ID informado.

### POST /produto

Cria um produto informando nome e preço.

Exemplo:

```text
/produto?nome=Mouse&preco=150