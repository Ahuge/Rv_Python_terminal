from PySide import QtGui
from widget_output_console import OutputConsole
from widget_input_console import InputConsole
import code


class ConsoleDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super(ConsoleDialog, self).__init__(*args, **kwargs)

        # create widgets
        self.console_widget = ConsoleWidget(self)

        # create layouts
        self.top_layout = QtGui.QVBoxLayout(self)

        # set properties
        self.setWindowTitle("Rv Python Console")
        self.top_layout.setSpacing(0)
        self.top_layout.setContentMargins(0, 0, 0, 0)


class ConsoleWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        # create widgets
        self.clear_button = QtGui.QPushButton("Clear")
        self.output_console = OutputConsole()
        self.input_console = InputConsole(
            appname="Rv Python Terminal",
            interpreter=code.InteractiveConsole(),
            stdout=self.output_console.stdin
        )

        # create layouts
        self.top_layout = QtGui.QVBoxLayout(self)

        # connect layouts
        self.top_layout.addWidget(self.input_console)
        self.top_layout.addWidget(self.output_console)
        self.top_layout.addWidget(self.clear_button)

        # connect signals
        self.input_console.CODE_EXECUTED.connect(self.output_console.read_stdin)
        self.clear_button.clicked.connect(self.output_console.clear)
