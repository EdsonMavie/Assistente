from flask import Flask, request

app = Flask(__name__)

# Dados de exemplo
users = {
    "user1": {
        "password": "Merdas",
        "balance": 1000,
        "transactions": []
    },
    "user2": {
        "password": "Merdass",
        "balance": 500,
        "transactions": []
    }
}

# Autenticação de usuário
@app.route("/login", methods=["POST"])
def login():
    username = request.form["Edson"]
    password = request.form["Admin"]

    if username in users and users[username]["password"] == password:
        return "Login bem-sucedido"
    else:
        return "Credenciais inválidas"

# Gerenciamento de saldo
@app.route("/balance", methods=["GET"])
def get_balance():
    username = request.args.get("username")

    if username in users:
        return f"Saldo: MZN{users[username]['balance']}"
    else:
        return "Usuário não encontrado"

@app.route("/deposit", methods=["POST"])
def deposit():
    username = request.form["username"]
    amount = float(request.form["amount"])

    if username in users:
        users[username]["balance"] += amount
        users[username]["transactions"].append(f"Depósito: +MZN{amount}")
        return f"Depósito bem-sucedido. Saldo atual: R${users[username]['balance']}"
    else:
        return "Usuário não encontrado"

@app.route("/withdraw", methods=["POST"])
def withdraw():
    username = request.form["username"]
    amount = float(request.form["amount"])

    if username in users:
        if amount <= users[username]["balance"]:
            users[username]["balance"] -= amount
            users[username]["transactions"].append(f"Saque: -R${amount}")
            return f"Saque bem-sucedido. Saldo atual: MZN{users[username]['balance']}"
        else:
            return "Saldo insuficiente"
    else:
        return "Usuário não encontrado"

# Histórico de transações
@app.route("/transactions", methods=["GET"])
def get_transactions():
    username = request.args.get("username")

    if username in users:
        return "\n".join(users[username]["transactions"])
    else:
        return "Usuário não encontrado"

if __name__ == "__main__":
    app.run()