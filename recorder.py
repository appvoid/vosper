# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
from os import system as cmd

class new:
    def __init__(self, waiting_time=4, filename='speaker'):
        # initialize recording so we can use it later
        self.recording = sd.rec(int(0 * 44100), samplerate=44100, channels=2)
        self.waiting_time = waiting_time # set a default waiting time
        self.filename = filename

    def record (self, waiting_time=4):
        # we set the same waiting time for the method
        self.waiting_time = waiting_time
        # setup recording
        self.recording = sd.rec(int(self.waiting_time * 44100), samplerate=44100, channels=2)

    def save (self):
        # save the new file
        write(f'{self.filename}.wav',44100,self.recording)
    
    def stop(self):
        # remove file so previous data doesn't get mixed up
        cmd(f'rm {self.filename}.wav >/dev/null 2>&1')
        # stop recording
        sd.stop()
        # finally, we save the file
        self.save()
