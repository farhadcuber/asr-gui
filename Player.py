import pyaudio
import wave
import threading
import atexit
from AudioConverter import AudioConverter

class Player(object):
    def __init__(self, inFile, interactiveUI, rate=44100):
        self.rate = rate
        self.wf = wave.open(AudioConverter(inFile), 'rb')

        self.slider = interactiveUI.ui.horizontalSlider
        self.interactiveUI = interactiveUI
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.wf.getnframes())
        self.slider.setValue(0)
        self.numFrames = 0

        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                                  channels=self.wf.getnchannels(),
                                  rate=self.wf.getframerate(),
                                  output=True,
                                  stream_callback=self.new_frame)
        self.stop = False
        self.pause = False
        atexit.register(self.close)

    def new_frame(self, data, frame_count, time_info, status):
        self.numFrames = self.numFrames + frame_count
        self.slider.setValue(self.numFrames)

        data = self.wf.readframes(frame_count)
        
        len_default = 2048
        if len(data) < len_default:
            self.stop = True
            self.interactiveUI.playerDone.done()

        return (data, pyaudio.paContinue)

    def close(self):
        
        self.stream.close()
        self.wf.close()
        self.p.terminate()
        
