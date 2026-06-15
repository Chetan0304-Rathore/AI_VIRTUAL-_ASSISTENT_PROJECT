import speech_recognition as sr
import webbrowser
import pyttsx3 # text to speechim
import musicLibrary
# pip install pocketspinix 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

 
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://open.whatspp.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =musicLibrary.music[song]    
        webbrowser.open(link)
    
if __name__ =="__main__":
    speak("Initializing jarvis...")
    while True:
        # listen for the wake word "jarvis "
        # optain audio from the microphone 
        r = sr.Recognizer()
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source,timeout=5,phrase_time_limit=3)# 
            word= r.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Yes")
                # listen for command 
                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
            
        
        except Exception as e:
            print("error; {0}".format(e))


                