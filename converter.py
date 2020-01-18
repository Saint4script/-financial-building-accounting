
from PyQt5 import QtWidgets
from zikkurat001 import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
 
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Build.clicked.connect(self.BuildFunc)
        
    def BuildFunc(self):
        print(self.ui.Project_cost.text())
        if(self.ui.Project_cost.text() == ""):
            tmp = int(self.ui.Self_cost.text())*int(self.ui.Total_area.text())
            self.ui.Project_cost.setText(str(tmp))

        
        
    
    
        
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()



sys.exit(app.exec())