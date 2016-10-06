from console_dialog import ConsoleDialog
import logging
import rv

__author__ = 'ahughes'
__version__ = '0.1.36'

LOGGING_FORMAT = "%(name)s: %(filename)s [%(levelname)s]: %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.WARNING)
logger = logging.getLogger("RvTerminal")


class RvTerminal(rv.rvtypes.MinorMode):
    def __init__(self):
        rv.rvtypes.MinorMode.__init__(self)
        self.init("Rv Python Terminal", None, None,
                  [("Tools",
                    [("Show Python Terminal", self.activate, "", None)])])

        self.dialog = ConsoleDialog()

    def activate(self):
        print("Activating QConsole v%s" % __version__)
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
    from Rv_Python_terminal import QtGui

    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])
    d = ConsoleDialog()
    d.show()
    app.exec_()
