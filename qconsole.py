from PySide import QtCore, QtGui
import logging

__author__ = 'ahughes'
__version__ = '0.1.52'
__sub_modules__ = ["third_party"]

# This is my hack to get around RV not opening up sub modules. :(
from lib_moving import force_lib_copying
for mod in __sub_modules__:
    force_lib_copying(file_=__file__, package_name=mod, version=__version__)

from third_party.QtPythonConsole.console import ConsoleWidget
try:
    import rv

    LOGGING_FORMAT = "%(name)s: %(filename)s [%(levelname)s]: %(message)s"
    logging.basicConfig(format=LOGGING_FORMAT, level=logging.WARNING)
    logger = logging.getLogger("RvTerminal")


    class RvTerminal(rv.rvtypes.MinorMode):
        def __init__(self):
            rv.rvtypes.MinorMode.__init__(self)
            self.init("Rv Python Terminal", None, None,
                      [("Terminal",
                        [("Show Python Terminal", self.toggle, None, self._state)])])

            self.title = QtGui.QLabel("Python Terminal")
            self.title.setStyleSheet("QLabel {margin-left: 50%; margin-right: 50%;}")
            self.dialog = QtGui.QDockWidget()
            self.dialog.setTitleBarWidget(self.title)
            self.widget = ConsoleWidget()
            self.dialog.setWidget(self.widget)
            self._visible = False
            self.readPrefs()
            self.dialog.visibilityChanged.connect(self.setVisible)

        def readPrefs(self):

            self._visible = bool(rv.commands.readSettings("Rv Python Terminal", "visible", False))

        def writePrefs(self):

            rv.commands.writeSettings("Rv Python Terminal", "visible", self._visible)

        def setVisible(self, visible):
            self._visible = visible

        def toggle(self, event):
            self._visible = not self._visible
            if self._visible:
                self.dialog.show()
            else:
                self.dialog.hide()
            self.writePrefs()

        def _state(self):
            if self._visible:
                return rv.commands.CheckedMenuState
            return rv.commands.UncheckedMenuState

        def activate(self):
            print("Activating QConsole v%s" % __version__)
            try:
                rv.rvtypes.MinorMode.activate(self)
                window = rv.qtutils.sessionWindow()
                window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dialog)
                self.dialog.hide()
            except Exception as e:
                print("-" * 50)
                print(str(e))
                print("-" * 50)

        def deactivate(self):
            print("Deactivating QConsole")
            window = rv.qtutils.sessionWindow()
            window.removeDockWidget(self.dialog)
            self.dialog.hide()
            rv.rvtypes.MinorMode.deactivate(self)


    def createMode():
        """
        Required to initialize the module. RV will call this function to create your mode.
        """
        print("Adding RvTerminal")
        return RvTerminal()
except:
    pass


if __name__ == "__main__":
    app = QtGui.QApplication.instance()
    if not app:
        app = QtGui.QApplication([])

    window = QtGui.QMainWindow()
    dialog = QtGui.QDockWidget()
    dialog.setTitleBarWidget(QtGui.QLabel("Python Terminal"))
    widget = ConsoleWidget()
    dialog.setWidget(widget)
    window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dialog)
    # d = ConsoleDialog()
    # d.show()
    window.show()
    app.exec_()
