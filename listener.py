# VOSK + Whisper speech recognition system
'''This module utilizes vosk as user feedback as well as VAD solution
    While it uses OpenAI whisper for actual transcription.'''

import os, pyaudio, whisper, recorder
from vosk import SetLogLevel, Model, KaldiRecognizer
SetLogLevel(-1)

whisp = whisper.load_model("small")
transcribing_whisper = False
recording_whisper = False

def load (model='small'):
    # load vosk model
    model_voice = Model(os.getcwd()+"/models/vosk/"+model)
    recognizer = KaldiRecognizer(model_voice, 16000)
    print('Model loaded')
    return recognizer

def Stream(listening=True):
    mic = pyaudio.PyAudio()
    # microphone streaming
    stream = mic.open(
        channels=1, 
        rate=16000, 
        input=True,
        format=pyaudio.paInt16,
        frames_per_buffer=4096
    )
    stream.start_stream()
    os.system('clear')
    return stream

def listen (data, recognizer):
    global recording_whisper
    data = data.read(4096)
    if recognizer.AcceptWaveform(data):
        recorder.stop()
        text = recognizer.Result()[14:-3]
        if (len(text) > 3):
            text = whisp.transcribe('speaker.wav')['text'].strip()
        recording_whisper = False

    else:
        text = recognizer.PartialResult()[17:-3]
        if (recording_whisper == False):
            recorder.stop()
            recording_whisper = True
            recorder.record(5)
    if text != '-' and text != '- ':
        return text
    else:
        return ''
