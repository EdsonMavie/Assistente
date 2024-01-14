import pyttsx3
import speech_recognition as sr
from fuzzywuzzy import fuzz
import random

# Lista de piadas adicionais
piadas_adicionais = [
    "Por que o computador foi ao médico? Porque estava com vírus!",
    "O que o advogado do frango foi fazer na delegacia? Foi soltar a franga!",
    "Por que o livro de matemática cometeu suicídio? Porque tinha muitos problemas!",
    "Qual é o cúmulo para um eletricista? Ficar chocado com o trabalho!",
    "O que o tomate foi fazer no banco? Foi tirar extrato!",
    "Como se chama o cúmulo da rapidez? Cair de costas!",
    "Qual é o contrário de volátil? É quando cai no chão!",
    "Por que o esqueleto não brigou com ninguém? Porque não tinha estômago para isso!",
    # Adicione mais piadas aqui
]
# Versiculos Biblicos
palavra_de_Deus = [
    "ATOS 2. 42  E perseveravam na doutrina dos apóstolos, e na comunhão, e no partir do pão, e nas orações. 43  E em toda a alma havia temor, e muitas maravilhas e sinais se faziam pelos apóstolos. 44  E todos os que criam estavam juntos, e tinham tudo em comum. 45  E vendiam suas propriedades e bens, e repartiam com todos, segundo cada um havia de mister. 46  E, perseverando unânimes todos os dias no templo, e partindo o pão em casa, comiam juntos com alegria e singeleza de coração, 47  Louvando a Deus, e caindo na graça de todo o povo. E todos os dias acrescentava o Senhor à igreja aqueles que se haviam de salvar!",
    "TIAGO 4. 7  Sujeitai-vos, pois, a Deus, resisti ao diabo, e ele fugirá de vós. 8  Chegai-vos a Deus, e ele se chegará a vós. Alimpai as mãos, pecadores; e, vós de duplo ânimo, purificai os corações!",
    "MATEUS 25. O sermão profético continua: A parábola das dez virgens. 1  ENTÃO o reino dos céus será semelhante a dez virgens que, tomando as suas lâmpadas, saíram ao encontro do esposo. 2  E cinco delas eram prudentes, e cinco loucas. 3  As loucas, tomando as suas lâmpadas, não levaram azeite consigo. 4  Mas as prudentes levaram azeite em suas vasilhas, com as suas lâmpadas. 5  E, tardando o esposo, tosquenejaram todas, e adormeceram. 6  Mas à meia-noite ouviu-se um clamor: Aí vem o esposo, saí-lhe ao encontro. 7  Então todas aquelas virgens se levantaram, e prepararam as suas lâmpadas. 8  E as loucas disseram às prudentes: Dai-nos do vosso azeite, porque as nossas lâmpadas se apagam. 9  Mas as prudentes responderam, dizendo: Não seja caso que nos falte a nós e a vós, ide antes aos que o vendem, e comprai-o para vós. 10  E, tendo elas ido comprá-lo, chegou o esposo, e as que estavam preparadas entraram com ele para as bodas, e fechou-se a porta. 11  E depois chegaram também as outras virgens, dizendo: SENHOR, Senhor, abre-nos. 12  E ele, respondendo, disse: Em verdade vos digo que vos não conheço!",

]
# Função para escolher uma piada aleatória
def escolher_piada_aleatoria():
    return random.choice(piadas_adicionais)
def dizer_a_palavra_de_Deus():
    return random.choice(palavra_de_Deus)

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
    return similarity_ratio > 80

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
            versiculos = dizer_a_palavra_de_Deus()
        elif check_similarity(command, "Conte me uma piada"):
            piada = escolher_piada_aleatoria()  # Escolher uma piada aleatória
            speak(piada)
        elif check_similarity(command, "apresente-se"):
            speak("Meu nome é Jarvis. A minha missão é servir a si Edson, desde já em que posso ajudar?")
        elif check_similarity( command, "Quem é o melhor memeiro do país?"):
            speak("O seu presidente baixinho. 2081 hahahaha")
        else:
            speak("Desculpe, não entendi o comando.")

if __name__ == "__main__":
    main()