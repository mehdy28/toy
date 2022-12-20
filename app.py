from flask import Flask, request
import speech_recognition as sr
import pyttsx3
import datetime

app = Flask(__name__)

r = sr.Recognizer()
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.RequestError:
            return "Sorry, I am unable to process your request."

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/assistant', methods=['POST'])
def assistant():
    command = request.form['command']
    if command == 'hello':
        speak('Hello, how can I help you today?')
        return 'Hello, how can I help you today?'
    elif command == 'what is the time':
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('The current time is ' + time)
        return 'The current time is ' + time
    else:
        speak('Sorry, I am unable to process your request.')
        return 'Sorry, I am unable to process your request.'

if __name__ == '__main__':
    app.run()