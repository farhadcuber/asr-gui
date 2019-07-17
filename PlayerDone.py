from PyQt4.QtCore import QObject, pyqtSignal, pyqtSlot
 
class PlayerDone(QObject):
    playerDone = pyqtSignal()
 
    def __init__(self):
        QObject.__init__(self)
 
    def done(self):
        self.playerDone.emit()