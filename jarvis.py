import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import webbrowser
import time

# ---------- TTS ----------
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)

def talk(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.6)

# ---------- LISTEN ----------
listener = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=0.5)
            audio = listener.listen(source)
        command = listener.recognize_google(audio).lower()
        return command
    except:
        return ""

# ---------- MAIN ----------
talk("Jarvis activated")

while True:
    command = listen()
    print("You said:", command)

    if command == "":
        continue

    # ---------- COMMANDS ----------
    if "time" in command or "date" in command:
        now = datetime.datetime.now()
        response = (
            now.strftime("Today is %A, %B %d, %Y. ")
            + now.strftime("The time is %I:%M %p.")
        )
        talk(response)
        time.sleep(1)

        

    elif "play" in command:
        song = command.replace("play", "").strip()
        talk(f"Playing {song}")
        
        
        pywhatkit.playonyt(song)

    elif "open google" in command:
        talk("Opening Google")
        
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        talk("Opening YouTube")
        
        webbrowser.open("https://www.youtube.com")

    elif "exit" in command or "stop" in command:
        
        talk("Goodbye")
        break

    else:
        talk("I did not understand")
