import pyaudio, array, math, time

RATE = 44100;

def writeOneBit(bit, freq, dur, toneArray):
    toneArray.extend(array.array('f', (math.sin(bit*i*2*math.pi/(RATE/freq)) for i in range(int(RATE*dur)))))
    
def playBitStream(bits, freq, dur):
    p = pyaudio.PyAudio()
    toneArray = array.array('f')
    for bit in bits:
        writeOneBit(bit, freq, dur, toneArray)
    start = time.time()
    stream = p.open(rate=RATE, channels=1, format=pyaudio.paFloat32, output=True)
    stream.write(toneArray.tostring())
    print time.time() - start
    stream.close()
    p.terminate()

if __name__ == '__main__':
    playBitStream([1, 1, 0, 1], 440, .25)
