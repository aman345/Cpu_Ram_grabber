
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
import sys
import time
import psutil
import icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(900, 500))
        self.centralwidget.setMaximumSize(QSize(900, 500))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(900, 100))
        self.header.setMaximumSize(QSize(900, 100))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.close_button_frames = QFrame(self.header)
        self.close_button_frames.setObjectName(u"close_button_frames")
        self.close_button_frames.setGeometry(QRect(760, 20, 121, 52))
        self.close_button_frames.setFrameShape(QFrame.StyledPanel)
        self.close_button_frames.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.close_button_frames)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.min = QPushButton(self.close_button_frames)
        self.min.setObjectName(u"min")
        self.min.setMinimumSize(QSize(20, 20))
        self.min.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/minus-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon)
        self.min.setFlat(True)

        self.horizontalLayout_2.addWidget(self.min)

        self.maximize_button = QPushButton(self.close_button_frames)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setMinimumSize(QSize(20, 20))
        self.maximize_button.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/layers.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.maximize_button)

        self.cross_button = QPushButton(self.close_button_frames)
        self.cross_button.setObjectName(u"cross_button")
        self.cross_button.setMinimumSize(QSize(20, 20))
        self.cross_button.setMaximumSize(QSize(20, 20))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cross_button.setIcon(icon2)
        self.cross_button.setFlat(True)
        

        self.horizontalLayout_2.addWidget(self.cross_button)

        self.application_label = QLabel(self.header)
        self.application_label.setObjectName(u"application_label")
        self.application_label.setGeometry(QRect(30, 35, 161, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.application_label.setFont(font)

        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)
        
        #body section of the application resides here 
        self.body = QFrame(self.centralwidget)
        self.body.setObjectName(u"body")
        self.body.setMinimumSize(QSize(900, 300))
        self.body.setMaximumSize(QSize(900, 350))
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cpu_usage = QFrame(self.body)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setMinimumSize(QSize(300, 600))
        self.cpu_usage.setMaximumSize(QSize(300, 600))
        self.cpu_usage.setFrameShape(QFrame.StyledPanel)
        self.cpu_usage.setFrameShadow(QFrame.Raised)
        self.rpb = roundProgressBar()
        self.rpb.rpb_setValue(25)   
        #self.horizontalLayout.addWidget(self.cpu_usage)
        self.horizontalLayout.addWidget(self.rpb)

        self.disk_usage = QFrame(self.body)
        self.disk_usage.setObjectName(u"disk_usage")
        self.disk_usage_layout = QVBoxLayout(self.disk_usage)
        self.disk_usage.setMinimumSize(QSize(300, 600))
        self.disk_usage.setMaximumSize(QSize(300, 600))
        self.disk_usage.setFrameShape(QFrame.StyledPanel)
        self.disk_usage.setFrameShadow(QFrame.Raised)
        #self.cpu_label = QLabel(self.disk_usage)
        #self.cpu_label.setObjectName(u"cpu_label")
        #self.cpu_label.setFont(font)
        self.rpb1 = roundProgressBar()
        self.disk_usage_layout.setSpacing(0)
        #self.disk_usage_layout.addWidget(self.cpu_label, -10,Qt.AlignTop)
        self.disk_usage_layout.addWidget(self.rpb1) 
        
        
        self.horizontalLayout.addWidget(self.disk_usage)

        self.memory_usage = QFrame(self.body)
        self.memory_usage.setObjectName(u"memory_usage")
        self.memory_usage.setMinimumSize(QSize(300, 300))
        self.memory_usage.setMaximumSize(QSize(300, 300))
        self.memory_usage.setFrameShape(QFrame.StyledPanel)
        self.memory_usage.setFrameShadow(QFrame.Raised)
        self.spbN = spiralProgressBar()    #SPIRAL PROGRESSBAR OBJECT
        self.spbN.spb_lineWidth(15)
        self.spbN.spb_setValue((55, 55, 55))
        self.horizontalLayout.addWidget( self.spbN)
        
        #properties of progress bars 
        self.rpb.rpb_setInitialPos('South')
        self.rpb1.rpb_setInitialPos('South') 
        self.rpb.rpb_setLineColor((28, 0, 128))
        self.rpb.rpb_setBarStyle('Line')
        self.rpb1.rpb_setLineColor((28, 0, 128))
        self.rpb1.rpb_setBarStyle('Hybrid2')
        self.rpb.rpb_setLineWidth(10)
        self.rpb1.rpb_setLineWidth(10)
        self.rpb.rpb_setLineCap('RoundCap')
        self.rpb1.rpb_setLineCap('RoundCap')
        self.spbN.spb_setInitialPos(('South', 'South', 'West'))
        self.spbN.spb_lineColor(((255, 0, 0),(2, 235, 0),(128,128,128)))
        self.spbN.spb_setPathHidden(True)
        self.max = 16
        self.spbN.spb_setMaximum((self.max, self.max, self.max))
        self.threadclass = ThreadClass(MainWindow)
        self.threadclass.start()
        #self.connect(self.threadclass,QtCore.SIGNAL("cpu_value"),self.updateProgressBar)
        self.threadclass.update_progress.connect(self.updateProgressBar)
        
        self.threadclass1 = ThreadRam(MainWindow)
        self.threadclass1.start()
        self.threadclass1.update_progress_ram.connect(self.updateprogressbarram)

        self.verticalLayout.addWidget(self.body)

        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMinimumSize(QSize(900, 50))
        self.footer.setMaximumSize(QSize(900, 50))
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.footer_label = QLabel(self.footer)
        self.footer_label.setObjectName(u"footer_label")
        self.footer_label.setGeometry(QRect(10, 20, 311, 16))

        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignHCenter|Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cross_button.clicked.connect(lambda:self.exit_app())
        self.min.clicked.connect(lambda:self.minimize())
        #self.cross_button.connect(self.exit_app())
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def updateprogressbarram(self,val):
        self.rpb1.rpb_setValue(val.percent) 
        self.spbN.spb_setValue((val.total/1024**3,val.available/1024**3,val.free/1024**3))
        #self.spbN.spb_setValue((10,20,50))
    
    def updateProgressBar(self,value):
        self.rpb.rpb_setValue(value) 
    
    def exit_app(self):
        self.threadclass.quit()
        self.threadclass1.quit()
        MainWindow.destroy()
        sys.exit(0)
    
    def minimize(self):
        MainWindow.showMinimized()
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fusion App", None))
        self.min.setText("")
        self.maximize_button.setText("")
        self.cross_button.setText("")
        self.application_label.setText(QCoreApplication.translate("MainWindow", u"Fusion Box ", None))
        #self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU Usage", None))
        self.footer_label.setText(QCoreApplication.translate("MainWindow", u"Application Version 1.0 | Open Source Lincensed", None))
    # retranslateUi
    
    

class ThreadClass(QtCore.QThread):
    update_progress =  QtCore.Signal(float)
    def __init__(self, pp):
        super(ThreadClass,self).__init__(pp)
    
    #run function of thread cycle
    def run(self):
       
        while 1:
            val = psutil.cpu_percent(interval=1)
            #for emiting the signal  for the application
            time.sleep(0.2)
            self.update_progress.emit(val)

class ThreadRam(QtCore.QThread):
    update_progress_ram =  QtCore.Signal(tuple)
    def __init__(self, pp):
        super(ThreadRam,self).__init__(pp)

    def run(self):
        while 1:
            value = psutil.virtual_memory()
            time.sleep(0.2)
            self.update_progress_ram.emit(value)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    widget = Ui_MainWindow()
    widget.setupUi(MainWindow )
    MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    MainWindow.show()
    sys.exit(app.exec_())
