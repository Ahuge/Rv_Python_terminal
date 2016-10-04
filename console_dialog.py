print("Starting Console Dialog")
from PySide import QtGui
from widget_output_console import OutputConsole
from widget_input_console import InputConsole


class ConsoleDialog(QtGui.QDialog):
    def __init__(self, *args, **kwargs):
        super(ConsoleDialog, self).__init__(*args, **kwargs)
        self.setWindowTitle("Rv Python Console")

        self.setLayout(QtGui.QVBoxLayout())
        output_console = OutputConsole()
        input_console = InputConsole(appname="Rv Python Terminal", stdout=output_console.stdin)
        input_console.CODE_EXECUTED.connect(output_console.read_stdin)

        self.layout().addWidget(input_console)
        self.layout().addWidget(output_console)
