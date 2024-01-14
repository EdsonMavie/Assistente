# Função para realizar a soma
def soma(a, b):
    return a + b

# Função para realizar a subtração
def subtracao(a, b):
    return a - b

# Função para realizar a multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

# Função para solicitar o login de usuário
def login():
    username = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    
    # Verificando se o login é válido (simplificado)
    if username == "Edson" and senha == "Merdas":
        return True
    else:
        return False

# Função principal
def main():
    if login():
        print("Login bem-sucedido!\n")
        while True:
            print("Escolha uma operação:")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")
            
            escolha = input("Digite o número da operação desejada: ")
            
            if escolha == "5":
                print("Saindo do programa.")
                break
            
            if escolha in ("1", "2", "3", "4"):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if escolha == "1":
                    resultado = soma(num1, num2)
                    print(f"Resultado da soma: {resultado}\n")
                elif escolha == "2":
                    resultado = subtracao(num1, num2)
                    print(f"Resultado da subtração: {resultado}\n")
                elif escolha == "3":
                    resultado = multiplicacao(num1, num2)
                    print(f"Resultado da multiplicação: {resultado}\n")
                elif escolha == "4":
                    resultado = divisao(num1, num2)
                    print(f"Resultado da divisão: {resultado}\n")
                else:
                    print("Opção inválida. Tente novamente.\n")
            else:
                print("Opção inválida. Tente novamente.\n")
    else:
        print("Login falhou. Verifique seu nome de usuário e senha.")

if __name__ == "__main__":
    main()
