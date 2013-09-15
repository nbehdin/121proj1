import numpy, pyaudio, analyse

RATE = 44100
perSec = 16
def readAudio(dur):
    pyaud = pyaudio.PyAudio()
    stream = pyaud.open(
        format = pyaudio.paInt16,
        channels = 1,
        rate = 44100,
        input_device_index = 0,
        input = True)
    sampsArray = []
    for i  in range(0, dur*perSec):
         # Read raw microphone data
        rawsamps = stream.read(RATE/perSec)
        # Convert raw data to NumPy array
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
        sampsArray.append(samps)
    print sampsArray
    return sampsArray

def postProcess(sampsArray):
    frequencies = []
    for samp in sampsArray:
        frequencies.append(analyse.detect_pitch(samp))
    return frequencies   

if __name__ == '__main__':
    samples = readAudio(1)
    frequencies = postProcess(samples)
    print frequencies
