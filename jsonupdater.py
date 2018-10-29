

from soundfunc import speak, recordAudio

import os

import json

def getusername():
    filename = 'knowledge.json'
    with open(filename, "r") as f:
        data = json.load(f)
    return(data.get('username'))

def getmagicword():
    filename = 'knowledge.json'
    with open(filename, "r") as f:
        data = json.load(f)
    return(data.get('magic word'))

def learning(data):
    data = data.split(" ")
    data = data[data.index("me") + 1:]
    question = ' '.join(data)
    print(question)
    filename = 'knowledge.json'
    with open(filename, "r") as f:
        data = json.load(f)

    if not data.get(question):

        # wait for next audio
        speak("Please input your ideas")
        temp_data = recordAudio()
        temp_data = temp_data.split(' ')
        data[question] = ' '.join(temp_data)  # <--- add question value.
        # Confirmation
        speak("You said " + ' '.join(temp_data) +  " are you sure")
        conf = recordAudio()
        if "yes" in conf:
            os.remove(filename)
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            return ('updated answer as ' +' '.join(temp_data))
        else: return ("no updates are made")

    else:
        return (data.get(question))

def override(data):
    data = data.split(" ")
    data = data[data.index("override") + 1:]
    key = ' '.join(data)
    print("overriding " + key)
    filename = 'knowledge.json'
    with open(filename, "r") as f:
        data = json.load(f)
    speak("Please input your new values")
    temp_data = recordAudio()
    temp_data = temp_data.split(' ')
    data[key] = ' '.join(temp_data)  # <--- add question value.
    speak("You said " + ' '.join(temp_data) + " are you sure?")
    conf = recordAudio()
    if "yes" in conf:
        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        return ('updated ' + key +' as ' + ' '.join(temp_data))
    else: return("no updates are made")