import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz
import random
from googlesearch import search

# ... (seu código existente)

# Função para realizar uma pesquisa na internet
def fazer_pesquisa(command):
    try:
        query = command.replace("pesquisar por", "")
        results = search(query, num_results=5)
        for i, result in enumerate(results, start=1):
            print(f"Resultado {i}: {result}")
            speak(f"Resultado {i}: {result}")
    except Exception as e:
        print(f"Erro ao realizar a pesquisa: {e}")
        speak("Desculpe, não consegui realizar a pesquisa.")

# Função principal do assistente
def main():
    speak("Olá! Em que posso ajudar?")
    
    while True:
        command = listen()
        
        if "parar" in command:
            speak("Até logo!")
            break
        
        # Adicione comandos e respostas aqui
        if check_similarity(command, "qual é o meu nome"):
            speak("O seu nome é Edson")
        if check_similarity(command, "Qual é o codigo do meu cartão?"):
            speak("O codigo é 0226")   
        if check_similarity(command, "Wifi da escola"):
            speak("95670492")    
        elif check_similarity(command, "como você está"):
            speak("Estou bem, obrigado por perguntar!")
        elif check_similarity(command, "fala a palavra de Deus"):
            versiculo = dizer_a_palavra_de_Deus()
            speak(versiculo)  # Fala o versículo da Palavra de Deus
        elif check_similarity(command, "Conte me uma piada"):
            piada = escolher_piada_aleatoria()  # Escolher uma piada aleatória
            speak(piada)
        elif check_similarity(command, "apresente-se"):
            speak("Meu nome é Jarvis. A minha missão é servir a você, Edson. Em que posso ajudar?")
        elif check_similarity( command, "Quem é o melhor memeiro do país?"):
            speak("O seu presidente baixinho. 2081 hahahaha")
        elif check_similarity(command, "pesquisar por"):
            fazer_pesquisa(command)
        else:
            speak("Desculpe, não entendi o comando.")

if __name__ == "_main_":
    main()