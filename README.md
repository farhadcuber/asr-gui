# SCL speech recognition GUI
Gui works with deepspeech2 engine running on docker.

## dependencies
1. ffmpeg
2. portaudio
3. pyaudio
4. python-qt4

## setup
1. install ```ffmpeg``` and ```python-qt4```:<br />
```sudo apt install ffmpeg python-qt4```
2. install ```portaudio``` using [link](https://medium.com/@niveditha.itengineer/learn-how-to-setup-portaudio-and-pyaudio-in-ubuntu-to-play-with-speech-recognition-8d2fff660e94).
3. create enviornment ```env``` inside directory.<br />
```virtualenv env```
4. install ```pyaudio```:<br />
```pip install pyaudio```
5. copy ```PyQt4``` files to ```env``` site-packages:
```
cp -r /usr/lib/python2.7/dist-packages/PyQt4/ env/lib/python2.7/site-packages/
cp /usr/lib/python2.7/dist-packages/sip* env/lib/python2.7/site-packages/
```