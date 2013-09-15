import numpy, pyaudio, analyse

RATE = 44100
perSec = 16

# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 2 is a USB microphone, your number may differ.
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True)

while True:
    # Read raw microphone data
    rawsamps = stream.read(RATE/perSec)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume and pitch
    print analyse.loudness(samps), analyse.detect_pitch(samps)
    
