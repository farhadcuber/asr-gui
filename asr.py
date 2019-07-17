import sys, os
from PyQt4 import QtCore, QtGui
from gui import Ui_Form
from MicrophoneRecorder import MicrophoneRecorder
from Player import Player
from PlayerDone import PlayerDone

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class IntractiveUI:
    def __init__(self, ui, pathToSpeech):
        self.ui = ui
        self.pathToSpeech = pathToSpeech
        self.openedFile = ''

        self.player = None
        self.recorder = None
        self.playerDone = PlayerDone()

        self.setConnections()

    def setConnections(self):
        self.ui.recButton.clicked.connect(self.recClicked)
        self.ui.playButton.clicked.connect(self.playClicked)
        self.ui.pauseButton.clicked.connect(self.pauseClicked)
        self.ui.openButton.clicked.connect(self.openFile)
        self.playerDone.playerDone.connect(self.donePlaying)

    def donePlaying(self):
        self.setText('[DONE] Audio played.')

    def recClicked(self):
        if (self.recorder == None or self.recorder.stop) and \
                (self.player == None or self.player.stop):
            self.startClicked()
        elif (self.recorder != None) and (not self.recorder.stop):
            self.stopClicked()

    def startClicked(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.recButton.setIcon(icon)
        self.ui.recButton.setIconSize(QtCore.QSize(50, 50))

        self.recorder = MicrophoneRecorder(self.pathToSpeech, rate=44100, \
            chunksize=1024)
            
        self.setText('[REC] Recording . . .')

    def stopClicked(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/record-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.recButton.setIcon(icon)
        self.ui.recButton.setIconSize(QtCore.QSize(50, 50))

        self.recorder.close()
        self.setText('[DONE] Saved to %s.' % self.pathToSpeech)
        self.openedFile = ''

    def playClicked(self):
        if (self.player == None or self.player.stop) and \
        (self.recorder == None or self.recorder.stop):
            
            if self.openedFile == '':
                fileToPlay = self.pathToSpeech
            else:
                fileToPlay = self.openedFile

            if not os.path.isfile(fileToPlay):
                self.setText('[ERR] %s doesn\'t exists.' % fileToPlay)

            self.player = Player(fileToPlay, self, rate=44100)

            self.setText('[PLAY] %s Playing . . .' % fileToPlay)

        elif self.player != None and self.player.pause:
            self.player.stream.start_stream()
            self.player.pause = False

    def pauseClicked(self):
        if self.player != None and (not self.player.pause):
            self.player.stream.stop_stream()
            self.player.pause = True

    def openFile(self):
    	fname = QtGui.QFileDialog.getOpenFileName(caption='Open File', \
    		filter='Audio files (*.wav *.mp3 *.flac)')
        if fname != '':
    	   self.setText('[DONE] %s is opened.' % fname)
    	   self.openedFile = str(fname)

    def setText(self, text):
        self.ui.textEdit.append(text)
        scrolBar = self.ui.textEdit.verticalScrollBar()
        scrolBar.setValue(scrolBar.maximum())

def atExit():
    os.system('rm recordings/*.tmp.wav')

app = QtGui.QApplication(sys.argv)
app.setWindowIcon(QtGui.QIcon('icons/icon.png'))

Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.setFixedSize(Form.size())


intractiveUI = IntractiveUI(ui, 'recordings/rec01.wav')
Form.destroyed.connect(atExit)

Form.show()
sys.exit(app.exec_())

