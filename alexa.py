import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import time

r = sr.Recognizer()

def alexeTalk(command):

    talk = pyttsx3.init()
    talk.say(command)
    talk.runAndWait()


def listening():
    with sr.Microphone() as source:
        print("Seni dinliyorum")
        record = r.listen(source)
        command = r.recognize_google(record)
        command = command.lower()
        if "alexa" in command:
            alexeTalk("what can I do for you?")
            with sr.Microphone() as soruce:
                record = r.listen(source)
                command = r.recognize_google(record)
                command = command.lower()
                command = command.replace("alexa","")
        return command

def run():
    while True:
        try:
            command = listening()
            if "play" in command:
                single = command.replace("play",'')
                alexeTalk("playing"+str(single))
                pywhatkit.playonyt(single)
            
            elif "search" in command:
                command = command.replace("search",'')
                result = wikipedia.summary(command)
                alexeTalk(result)
                print(result)
            
            elif "time" in command:
                time = datetime.datetime.now().strftime('%H %M')
                print(time)
                alexeTalk("Current time is" +time)
            
            elif "joke" in command:
                alexeTalk(pyjokes.get_joke())
            
            elif "close yourself" in command:
                alexeTalk("see you later")
                break
            print(command)
        except:
            print("Belirli sürede konuşmadınız veya anlaşılamadı lütfen tekrar deneyin")
            

run()
