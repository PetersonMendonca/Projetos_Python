''' INSTALAÇÕES SOBRE O TEMA
  # PyAudio - Para usar o microfone -> pip install PyAudio 
  # Pyttsx3 - Para gerar a sintese de fala -> pip install pyttsx3
  # SpeechRecognition - Reconhecimento online de alta qualidade, varios idiomas -> pip install SpeechRecognition
  # vosk - Reconhecimento de fala Offline -> pip install vosk
  # pyowm - Abre mapa meteriologico -> pip install pyowm
  # abre o google -> pip install google
  # abre o wikipedia -> pip install wikipedia-api
  # abre o google tradutor -> pip install googletrans
'''

''' AUTORES
  # Assistente Virtual - Com inteligencia artificial e reconhecimento de voz
  # Autores: André Luis Rodrigues e Peterson Mendonça de Oliveira
  # Data: 21/11/2021
  # Versão: 0.1.5
'''

import speech_recognition as reco
from gtts import gTTS
from playsound import playsound
import time
import datetime
import calendar
import wikipedia
import pyowm
import os


def dia_semana():
  curr_date = datetime.date.today()
  dia = calendar.day_name[curr_date.weekday()]

  match dia:
    case 'Sunday':
      return 'Domingo'
    case 'Monday':
      return 'Segunda'
    case 'Tuesday':
      return 'Terça'
    case 'Wednesday':
      return 'Quarta'
    case 'Thursday':
      return 'Quinta'
    case 'Friday':
      return 'Sexta'
    case 'Saturday':
      return 'Sabado'


def horas(frase):
  frase = time.strftime('São exatamente %H:%M:%S', time.localtime())
  print(frase)
  cria_audio(frase)
  
  
def dia_hoje(frase):
  nome_dia = dia_semana()
  frase = time.strftime(f'Hoje é {nome_dia} %Y-%m-%d', time.localtime())
  print(frase)
  cria_audio(frase)
  
  
def busca_wikipedia(frase):
  procurar = frase.replace('procure sobre', '')
  wikipedia.set_lang('pt')
  resultado = wikipedia.summary(procurar, sentences=2)
  resultado = 'Encontrei isso no Wikipedia' + resultado
  print(resultado)
  cria_audio(resultado)
  
  
def fechar(frase):
  frase = 'Tudo bem, volte sempre !'
  cria_audio(frase)
  
  
def nao_entendi():
  frase = 'Desculpa, não entendi, pode repetir!'
  cria_audio(frase)


def calcular(frase):
  frase_pergunta = 'Quanto deseja calcular?'
  cria_audio(frase_pergunta)
  
  frase = ouvir_microfone().lower().replace('x', '*')
  resu = eval(frase)
  
  frase = f'O resultado é {resu}'
  cria_audio(frase)
  
def Previsao_Tempo(frase):
  owm = pyowm.OWM('d9a6106d14fa576699d597498097565c')
  
  observation = owm.weather_at_place('Limeira,BR')
  w = observation.get_weather()
  print(w)
  w.get_temperature('celsius')
  print(w)
  pass


def cria_audio(audio):
  caminho_sons = "song/teste.mp3"                                                                                                              
  tts = gTTS(audio,lang='pt-br')
  tts.save(caminho_sons)
  playsound(caminho_sons)
  os.remove(caminho_sons)


def ouvir_microfone():                                                                                                       # Funcao responsavel por ouvir e reconhecer a fala
  microfone = reco.Recognizer()                                                                                              # Habilita o microfone para ouvir o usuario
    
  with reco.Microphone() as source:
    microfone.adjust_for_ambient_noise(source)                                                                               # Chama a funcao de reducao de ruido disponivel na speech_recognition
    print("\nOuvindo: ")                                                                                                     # avisa ao usuario que esta pronto para ouvir
    audio = microfone.listen(source,5,5)                                                                                     # Armazena a informacao de audio na variavel
    
    try:
      frase = microfone.recognize_google(audio,language='pt-BR')                                                             # Passa o audio para o reconhecedor de padroes do speech_recognition
      print("Você disse: " + frase)
      return frase
    except reco.UnknownValueError:                                                                                           # Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
      pass
      

## main
if __name__ == "__main__":
  
  while True:
    frase = ouvir_microfone()
    
    if frase.lower() == 'carla':
      frase = 'Oi, eu sou a Carla, em que posso te ajudar?'
      cria_audio(frase)
      
      while True:

        frase = ouvir_microfone()
        
        if frase.lower() in ['fechar', 'parar', 'fecha']:
          fechar(frase)
          break
        
        elif frase.lower() == 'que horas são':
          horas(frase)
          
        elif frase.lower() == 'que dia é hoje':
          dia_hoje(frase)
          
        elif frase.lower() in 'procure sobre':
          busca_wikipedia(frase)
        
        elif frase.lower() in 'calcule':
          calcular(frase)
        else:
          nao_entendi()
          
    elif frase.lower() in ['fechar', 'parar', 'fecha']:
      fechar(frase)
      break
    else:
      pass