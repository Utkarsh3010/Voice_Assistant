import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import os
import smtplib
import webbrowser

engine = pyttsx3.init('sapi5')  # engine-->to convert text to speech
voices = engine.getProperty('voices')  # to get the property of voices
engine.setProperty('voice', voices[0].id)  # set to set the voices 0--> for male and 1--> for female


def speak(audio):  # this will allow the things written by us to spoken
    engine.say(audio)
    engine.runAndWait()  # after program run it will wait to convert text into speech


def wishme():
    hour = int(datetime.datetime.now().hour)  # Gives the current time
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Evening")
    else:
        speak("Good Evening")
    speak("Let me Know how can i help you?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Gives access to your system Microphone
        print("Listening to you.....")
        r.pause_threshold = 1  # wait for sometime after listening
        audio = r.listen(source)
    try:
        print("Recognizing your voice......")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")
    except Exception as e:
        print("Please say it again.....")
        return "None"

    return query


def sendEmail(to, content):  # to-->to whom you want to send and content-->what you want to send
    server = smtplib.SMTP('smtp.gmail.com', 587)  # 587-->is the server
    server.ehlo()  # help in server
    server.starttls()  # it will start the server call through which we will be able to send email from here
    server.login()
    server.send()
    server.close()


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()  # take command and convert in lower case
        if 'open wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # start giving results and sentence-->read out first 2
            # sentence
            speak("According to wikipedia ")
            print(results)
            speak(results)
        if 'open notepad' in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)  # os startfile-->open the file

        elif 'open paint' in query:
            npath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(npath)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open hackerank' in query:
            webbrowser.open('https://www.hackerrank.com/access-account/')
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # strftime-->gives the format
            speak(f"the time is {strTime}")
        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")
        elif 'open github' in query:
            webbrowser.open("www.github.com")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/?hl=en")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")