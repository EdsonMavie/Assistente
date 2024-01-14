from googletrans import Translator

def traduzir(texto, destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=destino)
    return traducao.text

def responder_mensagem(mensagem):
    mensagem = mensagem.lower()

    if "olá" in mensagem:
        return "Olá! Como posso ajudar você?"

    elif "como você está" in mensagem:
        return "Estou apenas um programa de computador, mas estou aqui para ajudar! Como posso ser útil hoje?"

    elif "temperatura" in mensagem and "maputo" in mensagem:
        return "A temperatura em Maputo é de 25 graus Celsius."

    elif "factos curiosos" in mensagem:
        return "Sabia que os golfinhos são conhecidos por serem muito inteligentes e sociáveis?"

    elif "histórias bíblicas" in mensagem:
        return "Há muitas histórias bíblicas fascinantes, como a história de Noé e a Arca."

    elif "pesquisar" in mensagem:
        return "Desculpe, não sou capaz de fazer pesquisas no momento."

    else:
        return "Desculpe, não entendi. Como posso ajudar você?"

def main():
    print("Jarvis: Olá! Como posso ajudar você?")

    while True:
        mensagem_usuario = input("Você: ")
        mensagem_usuario_traduzida = traduzir(mensagem_usuario)
        resposta = responder_mensagem(mensagem_usuario_traduzida)
        resposta_traduzida = traduzir(resposta, destino='pt')
        print(f"Jarvis: {resposta_traduzida}")

        if "parar" in mensagem_usuario:
            print("Jarvis: Até logo!")
            break

if __name__ == "__main__":
    main()
C