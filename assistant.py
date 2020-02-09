import pyttsx3                    # packages you may required
import speech_recognition as sr   # pip install google-api-python-client
import datetime     			  # pip install PyAudio
import wikipedia                  # pip install wikipedia 
import webbrowser                 # pip install speechRecognition
import os                         # pip install pyttsx3
import smtplib                    # pip install monotonic
from random import randint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  #change the assistant voice [1],[0]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!,Hello Shaddy")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!Hi Shaddy")   

    else:
        speak("Good Evening! Hi Shaddy ")  
    speak("Tell me ..how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration = 1)
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio,language='en-us')
        print(f"I understand that:: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email_of_you@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

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

        elif 'open github' in query:
        	webbrowser.open("github.com/saif-15")

        elif 'play music' in query:
            music_dir = 'F:\\Songs'
            songs = os.listdir(music_dir)
            selected_song=randint(0,len(songs))
            speak(f"playing.{songs[selected_song]}")  
            os.startfile(os.path.join(music_dir,songs[selected_song]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%I:%M:%p")    
            speak(f"Shaddy, the time is {time}")

        elif 'the date' in query:
        	date=datetime.datetime.now().strftime("%A:%d:%B:%Y")
        	speak(f"Shaddy, the date is {date}")

        elif 'open vs' in query:
            codePath = "C:\\Users\\Shady\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to someone' in query:
            try:
                speak("What You want to say?")
                content = takeCommand()
                to = "to_whom_you_want_to_send@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry shady. I am not able to send this email")

        elif 'my name' in query:
        	speak("Hmmmmmmmmm.. you are Shaddy...I know You,")

        elif 'your name' in query:
        	speak("you dont know me...I am your assistant")

        else:
            print(query)    
