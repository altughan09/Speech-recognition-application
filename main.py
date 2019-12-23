import speech_recognition as sr
import webbrowser
import playsound
import os
import random
import time
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, a technical problem has been occurred')
        return voice_data


def speak(audio_string):
    tts = gTTS(audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'hi' in voice_data:
        speak('hello')
    if 'search' in voice_data:
        search = record_audio('Ok, what are you searching for?')
        url = 'https://www.google.com.pl/search?q=' + search
        webbrowser.get().open(url)
        speak('I found that ' + search)
    if 'thanks' in voice_data:
        speak('You are welcome')
    if 'close' in voice_data:
        speak('Closing')
        exit()

time.sleep(1)
speak('Hello, how can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
