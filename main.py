# Import modules
from vosk import Model, KaldiRecognizer
import pyaudio
import os

# Vosk
model = Model(r"/home/notjay/first-prototype/models/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 44000)

# Pyaudio
mic = pyaudio.PyAudio()

# Define callback
def callback(indata, frames, time, status):
    return (pyaudio.paContinue)

# Open stream using callback
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=44000, input=True, frames_per_buffer=22000)

# Start stream
stream.start_stream()

# Clear screen and print ready
os.system('clear')
print('Fully Initialized\nReady for input...\n')

# Print output
while True:
    data = stream.read(11000)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()

        print(text[14:-3])
