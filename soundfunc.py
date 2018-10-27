import speech_recognition as sr

import os

from gtts import gTTS

import re


def speak(audioString):
    print(audioString)
    audioString = re.sub('[!@#$?*@$:;.]', ' ', audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    r.energy_threshold = 4000
    #r.dynamic_energy_threshold = True # default True
    r.dynamic_energy_adjustment_damping = 0.3 # default 0.15
    r.dynamic_energy_adjustment_ratio = 1.5 #default 1.5
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("No command so far")
    except sr.RequestError as e:
        print("Could not request the input command; {0}".format(e))

    return data