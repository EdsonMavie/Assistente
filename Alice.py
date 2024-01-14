import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz

# Inicialize o motor de síntese de fala
engine = pyttsx3.init()

# Configurar a voz para português de Portugal
voices = engine.getProperty('voices')
for voice in voices:
    if "portugal" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

# Inicialize o reconhecedor de fala com o idioma "pt-PT"
recognizer = sr.Recognizer()

# Função para o assistente responder em voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para o assistente ouvir o comando de voz
def listen():
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language="pt-PT")
        print(f"Você disse: {command}")
        return command
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        return ""
    except sr.RequestError as e:
        print(f"Erro na solicitação: {e}")
        return ""

# Função para verificar correspondência aproximada de texto
def check_similarity(text, target):
    similarity_ratio = fuzz.ratio(text.lower(), target.lower())
    return similarity_ratio > 80  # Ajuste esse valor conforme necessário

# Função principal do assistente
def main():
    speak("Olá! Como posso ajudar você hoje?")
    
    while True:
        command = listen()
        
        if "parar" in command:
            speak("Até logo!")
            break
        
        # Adicione comandos e respostas aqui
        if check_similarity(command, "qual é o meu nome"):
            speak("O seu nome é Edson")
        elif check_similarity(command, "como você está"):
            speak("Estou bem, obrigado por perguntar!")
        elif check_similarity(command, "fala a palavra de Deus"):
            speak("ATOS 2. 42  E perseveravam na doutrina dos apóstolos, e na comunhão, e no partir do pão, e nas orações. 43  E em toda a alma havia temor, e muitas maravilhas e sinais se faziam pelos apóstolos. 44  E todos os que criam estavam juntos, e tinham tudo em comum. 45  E vendiam suas propriedades e bens, e repartiam com todos, segundo cada um havia de mister. 46  E, perseverando unânimes todos os dias no templo, e partindo o pão em casa, comiam juntos com alegria e singeleza de coração, 47  Louvando a Deus, e caindo na graça de todo o povo. E todos os dias acrescentava o Senhor à igreja aqueles que se haviam de salvar.")
        elif check_similarity(command, "Conte me uma piada"):
            speak("A enfermeira diz ao médico: Tem um homem invisível na sala de espera. O médico responde: Diga a ele que não posso vê-lo agora.")
        elif check_similarity(command, "conta outra"):
            speak("O condenado à morte esperava a hora da execução, quando chegou o padre: Meu filho, vim trazer a palavra de Deus para você. Perda de tempo, seu padre. Daqui a pouco vou falar com Ele pessoalmente. Algum recado?")
        elif check_similarity(command, "apresente-se"):
            speak("Meu nome é Jarvis. Estou aqui para servir a ti mestre Edson Mavihe")
        elif check_similarity( command, "Quem é o melhor memeiro do país?"):
            speak("O seu presidente baixinho. 2081 hahahaha")
        else:
            speak("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    main()
