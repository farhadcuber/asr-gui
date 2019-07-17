import pyaudio
import wave
import threading
import atexit

class MicrophoneRecorder(object):
    def __init__(self, outFile, rate=44100, chunksize=1024):
        self.outFile = outFile
        self.rate = rate
        self.chunksize = chunksize
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunksize,
                                  stream_callback=self.new_frame)
        self.lock = threading.Lock()
        self.stop = False
        self.frames = []
        atexit.register(self.close)

    def new_frame(self, data, frame_count, time_info, status):
        with self.lock:
            self.frames.append(data)
            if self.stop:
                return None, pyaudio.paComplete
        return None, pyaudio.paContinue
    
    def get_frames(self):
        with self.lock:
            frames = self.frames
            self.frames = []
            return frames
    
    def start(self):
        self.stream.start_stream()

    def save_frames(self):
        wf = wave.open(self.outFile, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def close(self):
        with self.lock:
            self.stop = True
        self.stream.close()
        self.save_frames()
        self.p.terminate()

