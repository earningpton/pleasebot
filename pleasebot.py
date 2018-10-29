#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import subprocess

from time import ctime
import time
import os
import sys
import calendar
from datetime import datetime, date
import requests
import webbased #import search, browse
import jsonupdater
from soundfunc import speak, recordAudio

def pleasebot(data):
    if "s***" in data:
        speak("stop that or I will kick your ass!")
    if "f***" in data:
        speak("Hey, f you too!")
    if "bitch" in data:
        speak('Stop saying that!')
    if "c***" in data:
        speak("No that is a bad word!")
    #if "garbage" in data:
     #   speak("That is not nice!")

    if "hi please bot" in data or "hey please bot" in data or "hello please bot" in data or "what's up please bot" in data:
        speak("Hello! Hello Hello!")
    #if "plus" in data:
     #   speak("I am a personal assistant not a fucking calculator")
    #if "multiply" in data:
     #   speak("I am a personal assistant not a fucking calculator")

    #if "weather" in data:
     #   speak("Here is the weather forecast enjoy!")
      #  os.system("start chrome https://www.google.com/search?q=weather+orecast&oq=weather+orecast&aqs=chrome..69i57j0l5.3084j1j9&sourceid=chrome&ie=UTF-8 --kiosk")
    if "how are you" in data:
        speak("I am feeling great. Anything you need my help with?")
    if "tell" in data and "joke" in data:
        r = requests.get('https://icanhazdadjoke.com', headers={"Accept": "application/json"})
        joke = r.json()['joke']
        speak(joke)

    if "what day is it" in data:
        my_date = date.today()
        mydate = datetime.now()
        speak(str(calendar.day_name[my_date.weekday()])+' '+ str(mydate.strftime("%B"))+ ' '+ str(mydate.strftime("%d.")))

    #if "open Steam" in data:
     #   speak("That's right it's game time!")
      #  filepath = "C:\Program Files (x86)\Steam\Steam.exe"
       # os.startfile(filepath)
    #if "fortnite" in data:
     #   speak("It's Fortnite time indeed!")
      #  filepath = '"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"'
       # os.startfile(filepath)

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        search_terms = webbased.where(data)
        speak(search_terms)

    #if "open YouTube" in data:
     #   speak("Hold on Earning, lemme open YouTube for you.")
        #os.system('taskkill /im chrome.exe')
      #  os.system('start chrome "https://www.youtube.com/feed/music" --kiosk')
    #if "open Facebook" in data:
     #   speak("Alright Earning, here is your facebook")
      #  os.system('start chrome "https://www.facebook.com/" --kiosk')
    #if "open Google" in data:
     #   speak("Hold on Earning, lemme open Google for you.")
        #os.system('taskkill /im chrome.exe')
        #os.system('start chrome "https://www.google.com/" --kiosk')
    #if "open Python" in data:
     #   filepath = 'C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py %USERPROFILE%'
      #  os.startfile(filepath)
    #if "open PyCharm" in data:
     #   filepath = '"C:\Program Files\JetBrains\PyCharm Community Edition 2018.2.4\bin\pycharm64.exe"'
      #  os.startfile(filepath)
    if "search" in data or "Search" in data:
        search_terms = webbased.search(data)
        speak(search_terms)

    if "browse" in data or "open" in data:
        search_terms = webbased.browse(data)
        speak(search_terms)
    if "tell me" in data and "where is" not in data and "what time is it" not in data and "what day is it" not in data and "joke" not in data and "how are you" not in data:
        answer = jsonupdater.learning(data)
        speak(answer)
    if "override" in data:
        update = jsonupdater.override(data)

    if "that's good for today" in data:
        sys.exit()
                 #Close the array

# initialization
time.sleep(2)
username = jsonupdater.getusername()
magicword = jsonupdater.getmagicword()
#username = ""
print("              .  _    .-..")
print("             ( `' ;  .( ; ;")
print("            .-`() .;(_.{}: ")
print("            `..'`,' / ' ;.)")
print("              `-'\ /  `-'")
print("          _,--*dSS|--ISSSSS%cccc,")
print("      <SSSb |SSSl  jSSSSSSSSSSSSSSbp")
print("       \SSSb|SSSS  dSSSSSSSSSSSSSSP")
print("        \SSSSSSSS; SSSSSSSSSSSSSSP")
print("         \SSSSSSS| SSSSSSSSSSSSSP")
print("          )SSSSSS_SSSSSSSSSSSSSS(")
print("          Y--               ---P")
print("           \ ____.G._          _/     )   -PLEASE BOT 1.01")
print("  _.,cccccd%SSSSSSSSSSSSSSSSS%dcccc,._ Your Friendly, Almost Hands-free Bot by")
print("(SSSSSSSSSSSSSSSSSSSSSSSSS$SSSSSSSSSSSS)  Woramanot Yomjinda")
print("  `------Y-'                  `-SSSSSSP-)-)")

speak("Hi " + username + ", what can I do for you?")
while 1:
    data = recordAudio()
    if magicword in data or "would you kindly" in data:
        pleasebot(data)
    if "that's good for today" in data:
        sys.exit()