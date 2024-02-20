import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound
import os
import wikipedia
from pynput.keyboard import *
import webbrowser as wb
import whisper


def Computer_speech(nkf):
    print(nkf)
    language = "de"
    output = gTTS(text=nkf, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")

def YouTube():
    pywhatkit.playonyt(text)

def BlueJ():
    dir1 = 'C:\BlueJ.exe'
    os.startfile(dir1)
    os.system(dir1)

def FallGuys():
    dir2 = 'steam://rungameid/1097150'
    os.startfile(dir2)
    os.system(dir2)

def Overwatch():
    dir3 = 'C:\Overwatch\Overwatch Launcher.exe'
    os.startfile(dir3)
    os.system(dir3)

def Excel():
    dir4 = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk'
    os.startfile(dir4)
    os.system(dir4)

def PowerPoint():
    dir5 = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk'
    os.startfile(dir5)
    os.system(dir5)

def Word():
    dir6 = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk'
    os.startfile(dir6)
    os.system(dir6)

def Steam():
    dir5 = 'D:\Steam\steam.exe'
    os.startfile(dir5)
    os.system(dir5)

def Information(topic, lines):
    wikipedia.set_lang("de")
    spe = wikipedia.summary(topic, sentences=lines)
    Computer_speech(spe)


def Google():
    pywhatkit.search(text)


def keyword():
    #while True:

    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("./sounds/activate.wav")
        print("listening...")
        audio = recorder.listen(source)

    global a
    a = 5

    global text
    text = recorder.recognize_google(audio, language="de-DE")
    print(f"You said: {text}")  # f am anfang vom print, wenn noch eine Variable geprintet werden soll
    return text


#text = keyword()



def op():
    if a == 5:
        print(a)

    if "computer" in text.lower():


        if "google" in text.lower():
            if "amazon" in text.lower():
                wb.open("https://amazon.de")

            if "youtube" in text.lower():
                wb.open("https://www.youtube.com/")

            if "twitch" in text.lower():
                wb.open("https://www.twitch.tv/")

            else:
               text = text.replace("Google", "")
               text = text.replace("Computer", "")
               Google()
               keyword()



        elif "youtube" in text.lower():
            YouTube()


        #Tastenkombinationen
        elif "leiser" in text.lower():
            keyboard = Controller()
            for i in range(30):
                keyboard.press(Key.media_volume_down)

        elif "lauter" in text.lower():
            keyboard = Controller()
            for i in range(30):
                keyboard.press(Key.media_volume_up)

        elif "letztes" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.media_previous)
            keyboard.press(Key.media_previous)

        elif "pause" in text.lower() or "hause" in text.lower() or "weiter" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.media_play_pause)

        elif "stumm" in text.lower()  or "laut" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.media_volume_mute)

        elif "letztes" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.media_previous)
            keyboard.press(Key.media_previous)

        elif "screenshot" in text.lower() and "alles" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.cmd)
            keyboard.press(Key.print_screen)
            keyboard.release(Key.print_screen)
            keyboard.release(Key.cmd)

        elif "screenshot" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.print_screen)
            keyboard.release(Key.print_screen)

        elif "desktop" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.cmd)
            keyboard.press('d')
            keyboard.release('d')
            keyboard.release(Key.cmd)

        elif "schließen" in text.lower():
            keyboard = Controller()
            keyboard.press(Key.alt)
            keyboard.press(Key.f4)
            keyboard.release(Key.f4)
            keyboard.release(Key.alt)


        elif "öffne" in text.lower():

            if "vollgas" in text.lower():
                FallGuys()

            if "blue" in text.lower():
                BlueJ()

            if "overwatch" in text.lower() or "rabac" in text.lower():
                Overwatch()

            if "excel" in text.lower():
                Excel()

            if "powerpoint" in text.lower():
                PowerPoint()


            if "word" in text.lower() or "rad" in text.lower() or "brad" in text.lower():
                Word()

            if "steam" in text.lower():
                Steam()


        elif "information" in text.lower() or "formation" in text.lower():
            text = text.replace("inforamtion", "")
            text = text.replace("Formation", "")

            if "kurz" in text.lower():
                text = text.replace("kurz", "")
                Information(topic = text, lines=1)

            else:
                Information(topic=text, lines=3)


    else:
        Computer_speech("K")

keyword()
op()