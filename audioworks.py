import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone as source:
        audio = r.listen(source)

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(f"Exception: {str(e)}")
    return said

speak("Hello welcome")

# get_audio()
