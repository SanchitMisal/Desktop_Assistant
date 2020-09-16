import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) #sirf ek hi voice h
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("Hello sir.Please tell me how may I help you")
def takeCommand():
    #it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 2
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("misterchauhan37@gmail.com","")#yha sender ka email likhna h
    server.sendmail('misterchauhan37@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    #speak("Harishanker is a good Boy.He is working on a project.")
    wishMe()
    i=0
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    while i<1:
        i=i+1
        query = takeCommand().lower()
        #logic for executing tasks on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            if 'tell me' in query:
                query=query.replace("tell me something about","")
                query=query.replace("from","")
                print("final query:",query)
            elif 'search' in query:

                query=query.replace("search something about","")
                query=query.replace("from","")
                print("final query:",query)
            else:
                speak("Unknown command.Please try again!!!!")
                sys.exit(0)
            results = wikipedia.summary(query,sentences=50)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'chrome' in query:
            os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            

        elif 'google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")
          

        elif 'play music' in query:
            music_dir = 'H:\\my utility'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[4]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Harishanker Chauhan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to chauhan' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "chauhan.oct98@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend.I am not able to send this email")

        elif 'quit' in query:
            sys.exit()


