

from logging import shutdown
import pyjokes
from numpy import number
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from requests import get
import pywhatkit



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir.. Please tell me how may I help you")      
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"Sir, the time is {strTime}")
 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('you email@gmail.com', 'password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

       
      

        elif 'work' in query:
            f = open('C:\\Users\\mmhus\\Downloads\\Jarvis\\dist\\my_work.txt','r')
            read = f.read()
            speak(read)
            print(read)
            f.close()

        elif 'w' in query:
            f = open('my_work.txt','a')
            speak('what to write')
            talk = takeCommand()
            f.write(talk )
            f.write(f'\n-------')
            f.close()


        elif 'jokes' in query:
            joke = pyjokes.get_jokes()
            speak(joke)
        elif 'shutdown' in query:
            os.system('shutdown / r/ t 5')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = "C:\\Users\\mmhus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'my number data' in query:
            os.startfile('C:\\Users\\mmhus\\Downloads\\Jarvis\\PyWhatKit_DB.txt')


        elif 'close' in query:
            speak('ok sir closing')
            command = takeCommand()
            os.system(f'taskkill /f /im {command}')
       
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input('Enter a email address : ')
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Talha. I am not able to send this email") 

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'ip is {ip}')

        elif 'exit' in query:
            break

        
        
