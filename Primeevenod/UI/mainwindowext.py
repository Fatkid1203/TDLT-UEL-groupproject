from Primeevenod.UI.mainwindow import Ui_MainWindow
from Primeevenod.Utils.functutils import filter_numbers

class mainwindowext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.Mainwindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.Mainwindow.show()

    def setupSignalAndSlot(self):
        self.process.clicked.connect(self.xuly_N)  # Kết nối nút nhấn với hàm xử lý
        self.prime.setText("")  # Đặt giá trị ban đầu cho các label
        self.even.setText("")
        self.odd.setText("")

    def xuly_N(self):
        try:
            N = int(float(self.N.text()))  # Nhận giá trị từ QLineEdit
            result = filter_numbers(N)

            # Gán kết quả cho các QLabel
            self.prime.setText(f"{', '.join(map(str, result[0]))}")
            self.even.setText(f"{', '.join(map(str, result[1]))}")
            self.odd.setText(f"{', '.join(map(str, result[2]))}")
        except ValueError:
            self.prime.setText("Invalid Data! Please input N again!")
            self.even.setText("Invalid Data! Please input N again!")
            self.odd.setText("Invalid Data! Please input N again!")

    # Hàm filter_numbers không thay đổi
