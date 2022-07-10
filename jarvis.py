from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random     #for play random music
import smtplib    # for sending mail 

engine = pyttsx3.init('sapi5') #sapi5 used to take voices (to use windows innbuit voice)
voices = engine.getProperty('voices') # we get the voices here
#print(voices) #2 voices hai (M/F)
engine.setProperty('voice', voices[1].id) #set the female voice (voice property set krna chah rha hu)
#print(voices[0])  #it prints the name of voice assistant
#print(voices[1])
                            #print(voices[2]) error

# audio dunga usko process krna hai. For that install pyttsx3 and import it
def speak(audio): 
    engine.say(audio)   #audio which is a string ko engine bolega
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour) #we will get hour (0-24). We imported datetime for that
    if hour>=0 and hour <12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis. Please tell me how may i help you")


#def takeCommand():   # for that we have to import speechRecognition module
    #it takes microphone input from the user and returns string output
  #  r = sr.Recognizer() #Recognizer class will help us to recognize voice from the microphone


def takeCommand():     # taking input from microphone and returns the string value
    #It take microphone input from the user and return string ouptut

    r =  sr.Recognizer() #Helps us to recognise the audio
    with sr.Microphone() as source:   #(source microphone ki taraha use krunga) 'with' automatically close the files we do not have to do this explicitly
        print("Listening....")
        r.pause_threshold = 2       #1 sec ka gap lelu toh kahi complete na krle
        audio = r.listen(source, timeout=1, phrase_time_limit=7)  

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')  # Using googel for voice recognisation this google engine is same as the engine we use in our phone 
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

#We will use smtplib for this
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('codeguyscode@gmail.com', 'Codeguyscode@12345') #for getting login
    server.sendmail('pamanbpl15@gmail.com', to, content)
    server.close() 


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1: 
        query = takeCommand().lower()
       
        #Logic for executing tasks based on query
        if 'wikipedia' in query:   # wikipedia is present in your query
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")  # jo query me wikipedia hai, use hata dunga
            results = wikipedia.summary(query, sentences=2) #return 2 sentence from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:  # for this we have web brower inbuilt module (web browser)
            webbrowser.open("youtube.com")
        elif 'open stack overflow' in query:  # for this we have web brower inbuilt module
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:  #have to use os module for that
            music_dir = 'D:\\Aman\\Gaane'
            songs = os.listdir(music_dir)
            print(songs)
            rand = random.randint(0, len(songs)- 1)
            os.startfile(os.path.join(music_dir, songs[rand]))  #os.startfile() khol dega us file ko aur music_dir ko mila dunga song[0] se

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pamanbpl15@gmail.com"
                sendEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
