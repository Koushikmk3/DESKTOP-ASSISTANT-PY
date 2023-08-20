import datetime
import os
import random
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import smtplib
#import mail_details as m

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path)) #add your preffered web browser path to be used to open sites

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if(hour <12):
        speak("Good Morning")
        e = "morning"
    elif(hour <18):
        speak("Good Afternoon")
        e = "afternoon"
    else:
        speak("Good Evening")
        e = "evening"
    speak("I am Stella, what can i do for you this %s" %e)


def takeCommand():

    """Function to recognize speech and convert it into 
    text which is passed as output from the function"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"interpreted: {query}\n")
    except Exception as e:
        print(e)
        speak("please say that again...")  # Block to handle excpetions
        print("please say that again...")
        return "None"
    return query


#def sendEmail(to,content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    #server.login(m.mail, m.password)
    #server.sendmail(m.mail, to, content)
    #server.close()


if __name__ == "__main__":
    wish()
    while(True):
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")

        elif 'play music' in query:
            #your local music directory path
            music_dir = "E:\\Songs"  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1) ] ))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'send email' in query:
            try:
                speak('what should i send?')
                content=takeCommand()
                to='recipientemail'  #Add reciever email
                #sendEmail(to,content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Could not send the mail')

        elif 'exit' in query:
            speak("have a good day")
            print("Have a good day!")
            break