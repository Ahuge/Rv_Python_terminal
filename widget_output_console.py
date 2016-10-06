from cStringIO import StringIO
from Rv_Python_terminal import QtCore, QtGui, QtWidgets
from widget_textedit import TextEdit


class OutputConsole(TextEdit):
    def __init__(self, parent=None):
        super(OutputConsole, self).__init__(parent)
        self.stdin = StringIO()
        self.setReadOnly(True)
        font = QtGui.QFont('courier', 9)
        self.setFont(font)
        pal = QtGui.QPalette()
        bgc = QtGui.QColor(50, 50, 50)
        pal.setColor(QtGui.QPalette.Base, bgc)
        text_color = QtGui.QColor(175, 175, 175)
        pal.setColor(QtGui.QPalette.Text, text_color)
        self.setPalette(pal)

    def read_stdin(self):
        # self.document().setPlainText(self.interpreter.process.stdout.read())
        self.document().setPlainText(self.stdin.getvalue())
        # self.stdin.truncate(0)

    def clear(self):
        self.stdin.truncate(0)
        self.document().setPlainText("")
