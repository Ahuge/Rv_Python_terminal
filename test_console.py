
#import sys
#sys.path.append('D:/alp/Projects/work/creaturecast')



if __name__ == '__main__':
    import sys
    from PySide import QtGui
    app = QtGui.QApplication(sys.argv)
    import Rv_Python_terminal.console_dialog as cdg

    console = cdg.ConsoleDialog(None)
    console.show()
    console.raise_()

    sys.exit(app.exec_())