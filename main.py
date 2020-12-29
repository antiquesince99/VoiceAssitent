import subprocess
import wolframalpha
import pyttsx3
import pyaudio
import tkinter
import json
import random
import operator
import speech_recognition as alexa
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import requests
import shutil
import pywhatkit
import requests, json
import weather_forecast as wf
listener = alexa.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
app = wolframalpha.Client("9XT567-6GQX55EQH3")
# def weather():
#
#     CITY = "LUCKNOW"
#     API_KEY = "7ca3c1af835f2867f4c76cdc52691df6"
#     BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q=" + CITY + "&appid=" + API_KEY
#     URL = BASE_URL+"q=" + CITY + "&appid=" + API_KEY
#     respose = requests.get(URL)
#     if respose.status_code==200:
#         data = respose.json()
#         main = data['main']
#         temprature = main['temp']
#         humidity = main['humidity']
#         pressure = main['pressure']
#         report = data['weather']
#         print(f"{CITY: -^30}")
#         print(f"temprature :{temprature}")
#         print(f"Humidity: {humidity}")
#         print(f"Pressure: {pressure}")
#         print(f"Weather Report: {report[0]['description']}")
#     else:
#         print("Error in the HTTP request")




def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    try:
        with alexa.Microphone() as source:
            print("alexa is Listening......")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command =command.replace('alexa','')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' +time)
    elif 'who is' in command:
        person = command.replace('who is','')
        information = wikipedia.summary(person, 1)
        print(information)
        talk(information)
    elif 'lets go for a date' in command:
        talk('sorry but i cant')
    elif 'are you single' in command:
        talk('I have a boyfriend')
    elif 'recipe' in command:
        dish = command.replace('recipe','')
        pywhatkit.playonyt(dish)
    elif 'jokes' in command:
        talk(pyjokes.get_jokes())
    elif 'weather' in command:
      try:
          res = app.query(command)
          print(next(res.results).text)
          talk(next(res.results).text)
      except Exception:
          print("Error occurs while connecting...")
    else:
        talk('Sorry Please Say It Again')


while True:
    run_alexa()
