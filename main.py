# Import modules
from vosk import Model, KaldiRecognizer
import pyaudio
import os

# Vosk
model = Model(r"/home/notjay/first-prototype/models/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 44000)

# Pyaudio
mic = pyaudio.PyAudio()

# Create and activate a virtualenv
virtualenv -p python3 $HOME/tmp/deepspeech-venv/
source $HOME/tmp/deepspeech-venv/bin/activate

# Install DeepSpeech
pip3 install deepspeech

# Download pre-trained English model files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.pbmm
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/deepspeech-0.9.3-models.scorer

# Download example audio files
curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.9.3/audio-0.9.3.tar.gz
tar xvf audio-0.9.3.tar.gz

# Transcribe an audio file
deepspeech --model deepspeech-0.9.3-models.pbmm --scorer deepspeech-0.9.3-models.scorer --audio audio/2830-3980-0043.wav

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
