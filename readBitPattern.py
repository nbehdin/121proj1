import numpy, pyaudio, analyse, time
from scipy.stats import mode

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
        #print sampsArray
    return sampsArray

def postProcess(sampsArray):
    frequencies = []
    for samp in sampsArray:
        frequencies.append(analyse.detect_pitch(samp))
    return frequencies   

def decode(frequencies, samples):
    print frequencies
    count = 0
    templist = []
    finallist = []
    for f in frequencies:
        if count % samples == 0 and templist:
           finallist.append(templist) 
           templist = [f]
        else:
            templist.append(f)
        count +=1
    finallist.append(templist)

    bits = []
    for bit in finallist:
        if mode(bit)[0][0] > 420 and mode(bit)[0][0] < 460:
            bits.append(1)
        else:
            bits.append(0)
    print bits
    
if __name__ == '__main__':
    start = time.time()
    samples = readAudio(1)
    frequencies = postProcess(samples)
    print "Time: " , time.time() - start
    decode(frequencies, 4)
    #print frequencies
    
