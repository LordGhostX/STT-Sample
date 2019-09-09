from os import remove
import speech_recognition as sr

def recognise_wav(wav_file):
    r = sr.Recognizer()

    src = sr.AudioFile(wav_file)
    with src as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    remove(wav_file)
    return text
