print("Starting QConsole")
from console_dialog import ConsoleDialog
import rv

__author__ = 'ahughes'
__version__ = '0.1.24'


class RvTerminal(rv.rvtypes.MinorMode):
    def __init__(self):
        rv.rvtypes.MinorMode.__init__(self)
        self.init("Rv Python Terminal", None, None,
                  [("Tools",
                    [("Show Python Terminal", self.activate, "", None)])])

        self.dialog = ConsoleDialog()

    def activate(self):
        print("Activating QConsole")
        try:
            rv.rvtypes.MinorMode.activate(self)
            self.dialog.show()
        except Exception as e:
            print("-" * 50)
            print(str(e))
            print("-" * 50)

    def deactivate(self):
        print("Deactivating QConsole")
        rv.rvtypes.MinorMode.deactivate(self)
        self.dialog.hide()


def createMode():
    """
    Required to initialize the module. RV will call this function to create your mode.
    """
    print("Adding RvTerminal")
    return RvTerminal()


if __name__ == "__main__":
    from PySide import QtGui
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    d = ConsoleDialog()
    d.show()
    app.exec_()
