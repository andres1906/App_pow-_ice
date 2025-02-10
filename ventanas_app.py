import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore

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

        # Quitar los iconos de minimizar, maximizar y cerrar
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)

        # Conectar los botones a funciones (manejadores de eventos)
        self.Ventas.clicked.connect(self.on_ventas_clicked)
        self.Compras.clicked.connect(self.on_compras_clicked)
        self.Administrar.clicked.connect(self.on_administrar_clicked)

    def on_ventas_clicked(self):
        self.ventas_window = Ventana1Window()
        self.ventas_window.show()
        self.hide()

    def on_compras_clicked(self):
        print("Botón 'Ingresar Compras' clickeado")

    def on_administrar_clicked(self):
        print("Botón 'Administrar' clickeado")

    def closeEvent(self, event):
        event.ignore()  # Ignorar el evento de cierre

def VentanaMain():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

# Clase generada por Qt Designer para page_v1
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

# Clase principal de la aplicación para page_v1
class Ventana1Window(QtWidgets.QWidget, Ui_page_v1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica

        # Conectar los botones a funciones (manejadores de eventos)
        self.Atras.clicked.connect(self.on_atras_clicked)
        self.OK.clicked.connect(self.on_ok_clicked)

    def on_atras_clicked(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def on_ok_clicked(self):
        user_id = self.username_in.text()
        if self.validate_user_id(user_id):
            self.user_ivalid.setText("Usuario válido")
        else:
            self.user_ivalid.setText("Usuario Invalido")

    def validate_user_id(self, user_id):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(1) FROM usuarios WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] > 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación
    main_window = MainWindow()  # Crea una instancia de la ventana principal
    main_window.setGeometry(100, 100, 720, 480)  # Define la posición y tamaño de la ventana
    main_window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos