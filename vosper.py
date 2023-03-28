# VOSK + Whisper speech recognition system
'''This module utilizes vosk as user feedback as wel as VAD solution
    While it uses OpenAI whisper for actual transcription.'''

# libraries
import os, pyaudio, whisper, recorder
from vosk import SetLogLevel, Model, KaldiRecognizer
SetLogLevel(-1) # mutes vosk verbosity
os.system('clear')
welcome_msg = '''\ \ / / _ \/ __| '_ \ / _ \ '__|
 \ V / (_) \__ \ |_) |  __/ |   
  \_/ \___/|___/ .__/ \___|_|   
               |_|  
                     by appvoid
'''

# debugging purposes
def log(msg, verbosity):
    if verbosity:
        print(msg)

class new:
    def load_vosk (self, model='small'):
        # load vosk model
        model_voice = Model(f'{os.getcwd()}/models/vosk/{model}')
        recognizer = KaldiRecognizer(model_voice, 16000)
        return recognizer

    def stream(self):
        mic = pyaudio.PyAudio()
        # microphone streaming

        '''this code is setting up an audio stream that 
        will capture mono audio at a sample rate of 16000 Hz 
        with 16-bit integer samples. It will capture audio 
        in chunks of 4096 samples at a time.'''

        _stream = mic.open(
            channels=1,
            rate=16000,
            input=True,
            format=pyaudio.paInt16, 
            frames_per_buffer=4096
        )
        _stream.start_stream()
        os.system('clear')
        return _stream

    def __init__(self, vosk_model='small', whisper_model='small.en', waiting_time=4, filename='speaker', verbosity=True):
        self.verbosity = verbosity
        log('- loading models...', self.verbosity)
        self.recorder = recorder.new(waiting_time, filename='speaker')
        self.whisper = whisper.load_model(whisper_model)
        self.vosk = self.load_vosk(vosk_model)
        self.recording_whisper = False
        self.filename = filename
        self.mic = self.stream()

        log(welcome_msg, self.verbosity)
        log(f'- waiting time:   {waiting_time} seconds\n- vosk model:     {vosk_model}\n- whisper model:  {whisper_model}\n- recording file: {filename}', self.verbosity)

    def listen (self):
        # we get data
        data = self.mic
        data = data.read(4096)

        # we check if person stopped talking from vosk recognizer
        if self.vosk.AcceptWaveform(data):
            self.recorder.stop() # we stop recording to save cpu compute
            text = self.vosk.Result()[14:-3]
            # we also check if the input does worth the whisper gpu compute
            characters_threshold = 3
            if (len(text) > characters_threshold):
                text = self.whisper.transcribe(f'{self.filename}.wav')['text'].strip()
            # we turn off whisper recognition variable
            self.recording_whisper = False

        else: # else, we show vosk text instead
            text = self.vosk.PartialResult()[17:-3]
            if (self.recording_whisper == False):
                self.recorder.stop()
                # we turn whisper on available for recording
                self.recording_whisper = True
                # we save 5 seconds of audio for whisper to transcribe
                self.recorder.record(5)
        
        # it's a simple but quite unbreakable spell 
        # for text checking to avoid printing empty strings
        if text != '-' and text != '- ':
            return text 
        else:
            return ''
