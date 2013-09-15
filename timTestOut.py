import pyaudio, array, math

RATE = 44100;
HZ = 440;

p = pyaudio.PyAudio()
stream = p.open(rate=44100, channels=1, format=pyaudio.paFloat32, output=True)
stream.write(array.array('f',
    (math.sin(i*2*math.pi/(RATE/HZ)) for i in range(44100))).tostring())
stream.close()
p.terminate()
