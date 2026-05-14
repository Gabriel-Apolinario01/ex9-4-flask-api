from flask import Flask, request, jsonify

app = Flask(__name__)

# rota principal
@app.route("/")
def home():
    return jsonify({
        "mensagem": "API Flask funcionando!"
    })

# GET usuários
@app.route("/usuarios", methods=["GET"])
def listar_usuarios():
    usuarios = ["Gabriel", "Maria", "João"]

    return jsonify({
        "usuarios": usuarios
    })

# GET usuário por id
@app.route("/usuario/<int:id>", methods=["GET"])
def buscar_usuario(id):
    return jsonify({
        "id": id,
        "nome": "Usuário Teste"
    })

# POST produto
@app.route("/produto", methods=["POST"])
def criar_produto():
    nome = request.args.get("nome")
    preco = request.args.get("preco")

    return jsonify({
        "mensagem": "Produto criado",
        "nome": nome,
        "preco": preco
    })

if __name__ == "__main__":
    app.run()