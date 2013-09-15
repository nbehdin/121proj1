import pyaudio, array, math, time

RATE = 44100;

def writeOneBit(bit, freq, dur, stream):
        stream.write(array.array('f', (math.sin(bit*i*2*math.pi/(RATE/freq)) for i in range(int(RATE*dur)))).tostring())

def playBitStream(bits, freq, dur):
    p = pyaudio.PyAudio()
    stream = p.open(rate=RATE, channels=1, format=pyaudio.paFloat32, output=True)
    for bit in bits:
        writeOneBit(bit, freq, dur, stream)
    stream.close()
    p.terminate()

if __name__ == '__main__':
    playBitStream([1, 1, 0, 1], 440, .25)
