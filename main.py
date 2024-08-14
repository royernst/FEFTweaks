import sys
from PyQt5 import QtWidgets
from GUI import MainForm

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
