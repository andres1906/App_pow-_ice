# main.py
import sys
from PyQt5 import QtWidgets, QtCore
from ventana1 import Ventana1Window

# Clase generada por Qt Designer para vmain
class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(400, 300)
        self.Ventas = QtWidgets.QPushButton(main)
        self.Ventas.setGeometry(QtCore.QRect(160, 50, 101, 24))
        self.Ventas.setObjectName("Ventas")
        self.Compras = QtWidgets.QPushButton(main)
        self.Compras.setGeometry(QtCore.QRect(150, 120, 121, 24))
        self.Compras.setObjectName("Compras")
        self.Administrar = QtWidgets.QPushButton(main)
        self.Administrar.setGeometry(QtCore.QRect(160, 180, 91, 24))
        self.Administrar.setObjectName("Administrar")

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Pow Ice main"))
        self.Ventas.setText(_translate("main", "Iniciar Ventas"))
        self.Compras.setText(_translate("main", "Ingresar Compras"))
        self.Administrar.setText(_translate("main", "Administrar"))

# Clase principal de la aplicación para vmain
class MainWindow(QtWidgets.QMainWindow, Ui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar los botones a funciones (manejadores de eventos)
        self.Ventas.clicked.connect(self.on_ventas_clicked)
        self.Compras.clicked.connect(self.on_compras_clicked)
        self.Administrar.clicked.connect(self.on_administrar_clicked)

    def on_ventas_clicked(self):
        self.ventas_window = Ventana1Window()
        self.ventas_window.show()
        self.close()

    def on_compras_clicked(self):
        print("Botón 'ingresar compas' clickeado")

    def on_administrar_clicked(self):
        print("Botón 'Administrar' clickeado")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    sys.exit(app.exec_())
