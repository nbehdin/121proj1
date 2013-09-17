import pyaudio, array, math, time
import numpy as np

RATE = 44100;

def writeOneBit(bit, freq, dur, toneArray, noiseStrength):
    toneArray.extend(array.array('f', (math.sin(bit*i*2*math.pi/(RATE/freq)+np.random.normal(0,noiseStrength,1 )) for i in range(int(RATE*dur)))))
    
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
def bitsToList(bits): 
    value = []
    for bit in bits:
        value.append(bit)
    return value
if __name__ == '__main__':
    playBitStream([1, 1, 0, 1], 440, .25)
    print np.random.normal(0,1,10)
