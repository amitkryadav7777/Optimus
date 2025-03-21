import pygame
import eel
import os
import re # to use regular expression
import time
import webbrowser
import pyttsx3
import sqlite3
import speech_recognition as sr
from backend.config import ASSISTANT_NAME
from backend.command import speak
import pywhatkit as kit

# Playing Optimus sound function

conn = sqlite3.connect("optimus.db")
cursor = conn.cursor()

@eel.expose
def playOptimusSound():

    pygame.mixer.init()

    music_dir = "template/assets/audio/start_sound.mp3"
    sound = pygame.mixer.Sound(music_dir)
    sound.play()
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

@eel.expose()
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "" :

        try :
            cursor.execute('SELECT path FROM sys_app_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("Not found")

        except:
            speak("Something went wrong!")

    # if(query!=""):
    #     engine = pyttsx3.init()
    #     speak("Opening "+query.capitalize())
    #     eel.DisplayMessage("Opening "+query.capitalize())
    #     time.sleep(2)
    #     os.system("Start "+query)
    # else:
    #     print(query.capitalize()+" not found")


def playYoutube(query) :
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" YouTube")
    kit.playonyt(search_term)

def extract_yt_term (command) :
    pattern = r'play\s+(.*?)\s+youtube'
    # pattern = r'play\s+(.*?)\s+(?:on\s+)?youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None