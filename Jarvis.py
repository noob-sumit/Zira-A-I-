import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    # it take microphone input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    
    except Exception as e:
        speak("can you say that again please")
        return "none"

    return query
    

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("good morning!")
    elif hour>=12 and hour <=18 :
        speak("good afternoon!")
    else:
        speak("good evening")
    
    speak("Hello Sumit sir, I am Zira, How may i help You")

if __name__ == "__main__":

    wish()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(f"according to wikipedia {results}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google ' in query:
            webbrowser.open("google.com")

        elif 'play online ' in query:
            webbrowser.open("https://www.youtube.com/watch?v=hBlO1i_WTiY&list=RDPicLAm0AWvE&index=6")

        elif 'play offline music' in query:
            music_dir = 'F:\\song'
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'quit' in query:
            exit()
         
        
        
    