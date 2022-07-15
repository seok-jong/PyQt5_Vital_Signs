import sys, random, time, os, sqlite3
import numpy as np
from PIL import Image
from ctypes import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import QStandardItem
from random import uniform, choice




class basic_window(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setGeometry(300, 300, 1280, 720)
        self.setWindowTitle('Vital Sign')

        # pal = QPalette()
        # pal.setColor(QPalette.Background, QColor(30, 30, 30))
        # self.setAutoFillBackground(True)
        # self.setPalette(pal)

class ui_main(basic_window):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.initUI()

        # self.thread1 = communication_thread(self)
        # self.thread1.start()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(0,0,0))
        qp.setPen(QPen(QColor(0,0,0)))
        qp.drawRect(0, 0, 1280, 720)
        

   
     
    def initUI(self):
        

        
        #-------------------------------------------------------
        
        
        
        self.Pulse_GB = QGroupBox("Heart Rate", self)
        self.Pulse_GB.move(50, 50)
        self.Pulse_GB.setFixedSize(350, 300)
        self.Pulse_GB.setFont(QFont("궁서",20))
        self.Pulse_GB.setStyleSheet('color : 	#FFFFFF;'
                                    'background-color: 	#9ACD32;'
                                    'border: 3px;'
                                    'border-radius: 10px;')

        self.Pulse_label1 = QLabel(self)
        self.Pulse_label1.setText('74')
        self.Pulse_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.Pulse_label1.setAlignment(Qt.AlignLeft)

        self.Pulse_label2 = QLabel(self)
        self.Pulse_label2.setText('bpm')
        self.Pulse_label2.setFont(QFont("궁서", 40,weight=QFont.Bold))
        self.Pulse_label2.setAlignment(Qt.AlignRight)

        self.Pulse_Hbox = QHBoxLayout()
        self.Pulse_Hbox.addWidget(self.Pulse_label1)
        self.Pulse_Hbox.addWidget(self.Pulse_label2)
        self.Pulse_Hbox.setAlignment(Qt.AlignCenter)

        self.Pulse_GB.setLayout(self.Pulse_Hbox)





#-------------------------------------------------------
        






        self.OS_GB = QGroupBox("SpO2 %", self)
        self.OS_GB.move(450, 50)
        self.OS_GB.setFixedSize(350, 300)
        self.OS_GB.setFont(QFont("궁서", 20))
        self.OS_GB.setStyleSheet('color : 	#FFFFFF;'
                                 'background-color: #4169E1;'
                                'border: 3px;'
                                'border-radius: 10px;')

        self.OS_label1 = QLabel(self)
        self.OS_label1.setText('98')
        self.OS_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.OS_label1.setAlignment(Qt.AlignLeft)

        self.OS_label2 = QLabel(self)
        self.OS_label2.setText('%')
        self.OS_label2.setFont(QFont("궁서", 40,weight=QFont.Bold))
        self.OS_label2.setAlignment(Qt.AlignRight)

        self.OS_Hbox = QHBoxLayout()
        self.OS_Hbox.addWidget(self.OS_label1)
        self.OS_Hbox.addWidget(self.OS_label2)
        self.OS_Hbox.setAlignment(Qt.AlignCenter)

        self.OS_GB.setLayout(self.OS_Hbox)






#-------------------------------------------------------
        






        self.PR_GB = QGroupBox("동공반응", self)
        self.PR_GB.move(850, 50)
        self.PR_GB.setFixedSize(350, 300)
        self.PR_GB.setFont(QFont("궁서", 20))
        self.PR_GB.setStyleSheet('color : 	#FFFFFF;'
                                 'background-color: green;'
                                ' border: 3px;'
                                'border-radius: 10px;')

        self.PR_label1 = QLabel(self)
        self.PR_label1.setText('정상')
        self.PR_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.PR_label1.setAlignment(Qt.AlignLeft)

        self.PR_Hbox = QHBoxLayout()
        self.PR_Hbox.addWidget(self.PR_label1)
        self.PR_Hbox.setAlignment(Qt.AlignCenter)

        self.PR_GB.setLayout(self.PR_Hbox)






#-------------------------------------------------------
        





        self.Temp_GB = QGroupBox("Temp ℃", self)
        self.Temp_GB.move(50, 400)
        self.Temp_GB.setFixedSize(350, 300)
        self.Temp_GB.setFont(QFont("궁서", 20))
        self.Temp_GB.setStyleSheet('color : 	#FFFFFF;'
                                   'background-color: #4B0082;'
                                ' border: 3px;'
                                'border-radius: 10px;')

        self.Temp_label1 = QLabel(self)
        self.Temp_label1.setText('36.3')
        self.Temp_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.Temp_label1.setAlignment(Qt.AlignLeft)

        self.Temp_label2 = QLabel(self)
        self.Temp_label2.setText('°C')
        self.Temp_label2.setFont(QFont("궁서", 40,weight=QFont.Bold))
        self.Temp_label2.setAlignment(Qt.AlignRight)
        
        # self.Temp_label3 = QLabel(self)
        print(self.Temp_label1)
        # self.Temp_label3.setText('36.3')
        # self.Temp_label3.setFont(QFont("궁서", 80,weight=QFont.Bold))
        # self.Temp_label3.setAlignment(Qt.AlignLeft)

        self.Temp_Hbox = QHBoxLayout()
        self.Temp_Hbox.addWidget(self.Temp_label1)
        self.Temp_Hbox.addWidget(self.Temp_label2)
        self.Temp_Hbox.setAlignment(Qt.AlignCenter)
        # setAlignment = 기본위치가 왼쪽/중간높이이지만 인자값을 통해 조절 가능 

        self.Temp_GB.setLayout(self.Temp_Hbox)





#-------------------------------------------------------
        





        self.RR_GB = QGroupBox("호흡수", self)
        self.RR_GB.move(450, 400)
        self.RR_GB.setFixedSize(350, 300)
        self.RR_GB.setFont(QFont("궁서", 20))
        self.RR_GB.setStyleSheet('color : 	#FFFFFF;'
                                 'background-color: green;'
                                ' border: 3px;'
                                'border-radius: 10px;')

        self.RR_label1 = QLabel(self)
        self.RR_label1.setText('13')
        self.RR_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.RR_label1.setAlignment(Qt.AlignLeft)

        self.RR_label2 = QLabel(self)
        self.RR_label2.setText('회/분')
        self.RR_label2.setFont(QFont("궁서", 40))
        self.RR_label2.setAlignment(Qt.AlignRight)

        self.RR_Hbox = QHBoxLayout()
        self.RR_Hbox.addWidget(self.RR_label1)
        self.RR_Hbox.addWidget(self.RR_label2)
        self.RR_Hbox.setAlignment(Qt.AlignCenter)

        self.RR_GB.setLayout(self.RR_Hbox)







#-------------------------------------------------------
        






        self.BP_GB = QGroupBox("Blood Pressure", self)
        self.BP_GB.move(850, 400)
        self.BP_GB.setFixedSize(500, 300)
        self.BP_GB.setFont(QFont("궁서", 20))
        self.BP_GB.setStyleSheet('color : 	#FFFFFF;'
                                 'background-color: #FF8C00;'
                                ' border: 3px;'
                                'border-radius: 10px;')

        self.BP_label1 = QLabel(self)
        self.BP_label1.setText('117')
        self.BP_label1.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.BP_label1.setAlignment(Qt.AlignLeft)

        self.BP_label2 = QLabel(self)
        self.BP_label2.setText('/')
        self.BP_label2.setFont(QFont("궁서", 80))
        self.BP_label2.setAlignment(Qt.AlignLeft)

        self.BP_label3 = QLabel(self)
        self.BP_label3.setText('79')
        self.BP_label3.setFont(QFont("궁서", 80,weight=QFont.Bold))
        self.BP_label3.setAlignment(Qt.AlignRight)

        self.BP_Hbox = QHBoxLayout()
        self.BP_Hbox.addWidget(self.BP_label1)
        self.BP_Hbox.addWidget(self.BP_label2)
        self.BP_Hbox.addWidget(self.BP_label3)
        self.BP_Hbox.setAlignment(Qt.AlignCenter)




#-------------------------------------------------------
        




        self.Pulse_GB.setLayout(self.Pulse_Hbox)
        self.OS_GB.setLayout(self.OS_Hbox)
        self.PR_GB.setLayout(self.PR_Hbox)
        self.Temp_GB.setLayout(self.Temp_Hbox)
        self.RR_GB.setLayout(self.RR_Hbox)
        self.BP_GB.setLayout(self.BP_Hbox)

        # self.btn = QPushButton('Check', self)
        # self.btn.resize(self.btn.sizeHint())
        # self.btn.setFixedSize(self.btn.sizeHint())
        # self.btn.clicked.connect(self.buttonFunction)

        self.show()

    # def buttonFunction(self):
    #     pulse_value = round(uniform(60.0, 80.0), 2)
    #     OS_value = round(uniform(95.0, 100.0), 2)
    #     PR_value = choice(['정상', '비정상'])
    #     Temp_value = round(uniform(35.0, 39.0), 2)
    #     RR_value = round(uniform(12.0, 20.0), 2)
    #     BP_high_value = round(uniform(100.0, 120.0), 1)
    #     BP_low_value = round(uniform(70.0, 80.0), 2)

    #     self.Pulse_label1.setText(str(pulse_value))
    #     self.OS_label1.setText(str(OS_value))
    #     self.PR_label1.setText(PR_value)
    #     self.Temp_label1.setText(str(Temp_value))
    #     self.RR_label1.setText(str(RR_value))
    #     self.BP_label1.setText(str(BP_high_value))
    #     self.BP_label3.setText(str(BP_low_value))


if __name__ == '__main__':
    # manager = multiprocessing.Manager()
    # lock = multiprocessing.Lock()

    # forehead_data_buffer = manager.list()
    # ueye_data_buffer = manager.list()
    # cheek_data_buffer = manager.list()
    # unose_data_buffer = manager.list()

    # # # Display UI
    app = QApplication(sys.argv)
    ui_main = ui_main()

    # # # Estimator Spo2
    # spo2_estimator = VitalSign_Spo2_Estimator.VitalSign_Spo2_Estimator(lock, ui_main.OS_label1, forehead_data_buffer, ueye_data_buffer, cheek_data_buffer, unose_data_buffer)
    # #
    # # Estimator Pulse
    # pulse_estimator = VitalSign_Pulse_Estimator.VitalSign_Pulse_Estimator(lock, ui_main.Pulse_label1, forehead_data_buffer, ueye_data_buffer, cheek_data_buffer, unose_data_buffer)
    # #
    # # Read data Process
    # proc = multiprocessing.Process(target=read_data_test.read_data, args=(lock, forehead_data_buffer, ueye_data_buffer, cheek_data_buffer, unose_data_buffer))
    # proc.start()

    sys.exit(app.exec_())
    proc.join()
