import sys
from PySide6.QtWidgets import QApplication
from controller import CounterController

def main():
    app = QApplication(sys.argv)
    controller = CounterController()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()