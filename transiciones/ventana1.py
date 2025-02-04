import sys
from PyQt5 import QtWidgets, QtCore
#from vmain import MainWindow

class Ui_page_v1(object):
    def setupUi(self, page_v1):
        page_v1.setObjectName("page_v1")
        page_v1.resize(400, 300)
        self.label = QtWidgets.QLabel(page_v1)
        self.label.setGeometry(QtCore.QRect(150, 40, 141, 31))
        self.label.setObjectName("label")
        self.username_in = QtWidgets.QLineEdit(page_v1)
        self.username_in.setGeometry(QtCore.QRect(160, 90, 113, 24))
        self.username_in.setObjectName("username_in")
        self.user_ivalid = QtWidgets.QLabel(page_v1)
        self.user_ivalid.setGeometry(QtCore.QRect(180, 130, 61, 16))
        self.user_ivalid.setText("")
        self.user_ivalid.setObjectName("user_ivalid")
        self.Atras = QtWidgets.QPushButton(page_v1)
        self.Atras.setGeometry(QtCore.QRect(220, 200, 91, 30))
        self.Atras.setObjectName("pushButton_2")
        self.OK = QtWidgets.QPushButton(page_v1)
        self.OK.setGeometry(QtCore.QRect(110, 200, 91, 30))
        self.OK.setObjectName("pushButton")

        self.retranslateUi(page_v1)
        QtCore.QMetaObject.connectSlotsByName(page_v1)

    def retranslateUi(self, page_v1):
        _translate = QtCore.QCoreApplication.translate
        page_v1.setWindowTitle(_translate("page_v1", "page_v1"))
        self.label.setText(_translate("page_v1", "Ingrese su Usuario"))
        self.Atras.setText(_translate("page_v1", "Atrás"))
        self.OK.setText(_translate("page_v1", "OK"))


class Ventana1Window(QtWidgets.QWidget, Ui_page_v1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica

'''
        #funciones de los botones
        self.Atras.cliked.connect(self.on_Atras_clicked)

    def on_Atras_clicked(self):
        self.Atras = MainWindow()
        self.Atras.show()
        self.close()
'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación
    window = Ventana1Window()  # Crea una instancia de la ventana principal
    window.setGeometry(100, 100, 400, 300)  # Define la posición y tamaño de la ventana
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos
