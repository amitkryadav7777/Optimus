import eel
import pyttsx3
import speech_recognition as sr
import time
import pywhatkit


def speak(text) :
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source,None)

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        eel.DisplayMessage(query)
        time.sleep(1)
        speak(query)

    except Exception as e:
        return "Sorry! I'm unable to understand."
    
    return query.lower()


@eel.expose()
def allCommands(message) :
    if message == "" :
        query = takeCommand()
        eel.senderText(query)
    else :
        query = message
        eel.senderText(query)

    if "open" in query:
        from backend.features import openCommand
        openCommand(query)
    elif "on Youtube" in query:
        from backend.features import playYoutube
        playYoutube(query)
    else:
        print("Not run")

    eel.ShowHood()


# text = takeCommand()
# speak(text)