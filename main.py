import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()


def record_audio(ask=False):
    # take our audio from microphone
    with sr.Microphone() as source:
        if ask:
            miili_speak(ask)
        audio = r.listen(source)
        voice_data = ""
        try:
            # performs speech recognition from the audio
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            miili_speak("Sorry, I did not get that")
        except sr.RequestError:
            miili_speak("Sorry, my speech service is down")
        return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        miili_speak("My name is Milli")
    if "what time is it" in voice_data:
        miili_speak(ctime())
    if "search" in voice_data:
        search = record_audio("What do you want to search for?")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        miili_speak("Here is what i found for " + search)
    if "find location" in voice_data:
        location = record_audio("What is the location?")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        miili_speak("Here is the location of " + location)
    if "exit" in voice_data:
        exit()


def miili_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 100000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


time.sleep(1)
miili_speak("Say something")
while 1:
    voice_data = record_audio()
    respond(voice_data)
