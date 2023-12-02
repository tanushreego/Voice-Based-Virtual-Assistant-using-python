import subprocess
from random import choice
from datetime import datetime
import speech_recognition as sr

USERNAME = 'HUMANS'
Vir_Asst = 'Wednesday'

# List of responses for working and thank you messages
working_text = ["Sure, I'm here to help.", "Of course!", "Absolutely.", "I can do that.", "No problem!"]
thank_you = ["You're welcome!", "No problem!", "Anytime!"]


# Greet the user
def greet_user():
    hour = datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USERNAME}")
        print(f"Good Morning {USERNAME}")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USERNAME}")
        print(f"Good Afternoon {USERNAME}")
    else:
        speak(f"Good Evening {USERNAME}")
        print(f"Good Evening {USERNAME}")
    speak(f"I am {Vir_Asst} your virtual assistant. How may I assist you?")
    print(f"I am {Vir_Asst} your virtual assistant. How may I assist you?")


# Function to speak using macOS 'say' command
def speak(text):
    subprocess.run(["say", text])


# Recognize user input
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        print("Listening to the microphone")
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not any(keyword in query.lower() for keyword in ['exit', 'stop', 'thanks', 'thank you']):
            speak(choice(working_text))
        else:
            if any(keyword in query.lower() for keyword in ['thanks', 'thank you']):
                speak(choice(thank_you))
            elif any(keyword in query.lower() for keyword in ['exit', 'stop']):
                hour = datetime.now().hour
                if 21 <= hour or hour < 4:
                    speak(f"Good night {USERNAME}, take care!")
                else:
                    speak(f'Have a good day {USERNAME}!')
                exit()
    except Exception:
        speak('Sorry, I am not able to understand that. Could you please say that again?')
        query = 'None'
    return query


# Main loop
if __name__ == "__main__":
    greet_user()
    while True:
        user_input = take_user_input()
        print("User said:", user_input)
