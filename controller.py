from PySide6.QtWidgets import QMessageBox, QMainWindow

from model import CounterModel
from view import Ui_root

class CounterController(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = CounterModel()

        # Load the Qt designer UI
        self.ui = Ui_root()
        self.ui.setupUi(self)

        # Connect the Buttons
        self.ui.btnIncrement.clicked.connect(self.increment)
        self.ui.btnDecrement.clicked.connect(self.decrement)

        self.show()

       

    def increment(self):
        amount = self.getInput()
        if amount is not None:
            self.model.increment(amount)
            self.setLabel()    
    
    def decrement(self):
        amount = self.getInput()
        if amount is not None:
            self.model.decrement(amount)
            self.setLabel()  

    def getInput(self):
        text = self.ui.entEdit.text()
        try:
            return int(text)
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter an integer.")
            return None

    def setLabel(self):
        self.ui.lblAmount.setText(str(self.model.getValue()))
