# import required libraries
import sounddevice as sd, os
from scipy.io.wavfile import write

recording = sd.rec(int(0 * 44100), samplerate=44100, channels=2)

def record (secs=4):
    global recording
    recording = sd.rec(int(secs * 44100), samplerate=44100, channels=2)

def stop():
    global recording
    sd.stop()
    os.system('rm speaker.wav')
    write('speaker.wav',44100,recording)