# vosper: a simple tool to easily get high-quality Automatic Speech Recognition using SOTA models
from os import system as cmd; import listener
mic, rec = listener.Stream(), listener.load('small') # you can download more realtime models here: https://alphacephei.com/vosk/models

while 'listening':
    _input = listener.listen(mic, rec)
    if ('-' in _input):
        print(_input)
    elif (_input != ''):
        cmd('clear'); print('- '+ _input)