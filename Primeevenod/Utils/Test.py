from PyQt6.QtWidgets import QApplication, QMainWindow

from Primeevenod.UI.mainwindowext import mainwindowext

app=QApplication([])
mainwindow=QMainWindow()
myui=mainwindowext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()