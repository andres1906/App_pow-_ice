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
        user_name = self.get_user_name(user_id)
        if user_name:
            self.user_ivalid.setText("Usuario válido")
            self.page_v2_window = Ventana2Window(user_name)
            self.page_v2_window.show()
            self.close()
        else:
            self.user_ivalid.setText("Usuario Invalido")

    def get_user_name(self, user_id):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM usuarios WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None

# Clase generada por Qt Designer para page_v2
class Ui_page_v2(object):
    def setupUi(self, page_v2):
        page_v2.setObjectName("page_v2")
        page_v2.resize(492, 342)
        self.user_active = QtWidgets.QLabel(page_v2)
        self.user_active.setGeometry(QtCore.QRect(20, 0, 300, 20))  # Ajustar la posición y el tamaño
        self.user_active.setObjectName("user_active")
        self.tableView = QtWidgets.QTableView(page_v2)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 121, 211))
        self.tableView.setObjectName("tableView")
        self.Helados = QtWidgets.QPushButton(page_v2)
        self.Helados.setGeometry(QtCore.QRect(160, 30, 91, 30))
        self.Helados.setObjectName("Helados")
        self.Paletas = QtWidgets.QPushButton(page_v2)
        self.Paletas.setGeometry(QtCore.QRect(160, 60, 91, 30))
        self.Paletas.setObjectName("Paletas")
        self.Obleas = QtWidgets.QPushButton(page_v2)
        self.Obleas.setGeometry(QtCore.QRect(160, 90, 91, 30))
        self.Obleas.setObjectName("Obleas")
        self.Brownie = QtWidgets.QPushButton(page_v2)
        self.Brownie.setGeometry(QtCore.QRect(160, 120, 91, 30))
        self.Brownie.setObjectName("Brownie")
        self.Waffles = QtWidgets.QPushButton(page_v2)
        self.Waffles.setGeometry(QtCore.QRect(160, 180, 91, 30))
        self.Waffles.setObjectName("Waffles")
        self.Fresas = QtWidgets.QPushButton(page_v2)
        self.Fresas.setGeometry(QtCore.QRect(160, 150, 91, 30))
        self.Fresas.setObjectName("Fresas")
        self.Bebidas = QtWidgets.QPushButton(page_v2)
        self.Bebidas.setGeometry(QtCore.QRect(160, 210, 91, 30))
        self.Bebidas.setObjectName("Bebidas")
        self.Otros = QtWidgets.QPushButton(page_v2)
        self.Otros.setGeometry(QtCore.QRect(160, 240, 91, 30))
        self.Otros.setObjectName("Otros")
        self.pushButton_2 = QtWidgets.QPushButton(page_v2)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 300, 91, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(page_v2)
        self.pushButton.setGeometry(QtCore.QRect(270, 300, 91, 30))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(page_v2)
        self.label.setGeometry(QtCore.QRect(20, 250, 68, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(page_v2)
        self.label_2.setGeometry(QtCore.QRect(70, 250, 68, 22))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(page_v2)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 280, 91, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(page_v2)
        QtCore.QMetaObject.connectSlotsByName(page_v2)

    def retranslateUi(self, page_v2):
        _translate = QtCore.QCoreApplication.translate
        page_v2.setWindowTitle(_translate("page_v2", "page_v2"))
        self.user_active.setText(_translate("page_v2", "usuario activo: _____"))
        self.Helados.setText(_translate("page_v2", "Helados"))
        self.Paletas.setText(_translate("page_v2", "Paletas"))
        self.Obleas.setText(_translate("page_v2", "Obleas"))
        self.Brownie.setText(_translate("page_v2", "Brownie"))
        self.Waffles.setText(_translate("page_v2", "Waffles"))
        self.Fresas.setText(_translate("page_v2", "Fresas"))
        self.Bebidas.setText(_translate("page_v2", "Bebidas"))
        self.Otros.setText(_translate("page_v2", "Otros"))
        self.pushButton_2.setText(_translate("page_v2", "Atrás"))
        self.pushButton.setText(_translate("page_v2", "OK"))
        self.label.setText(_translate("page_v2", "Total:"))
        self.label_2.setText(_translate("page_v2", "111111"))
        self.pushButton_3.setText(_translate("page_v2", "Borrar"))

# Clase principal de la aplicación para page_v2
class Ventana2Window(QtWidgets.QWidget, Ui_page_v2):
    def __init__(self, user_name):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica
        self.user_active.setText(f"usuario activo: {user_name}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación
    main_window = MainWindow()  # Crea una instancia de la ventana principal
    main_window.setGeometry(100, 100, 720, 480)  # Define la posición y tamaño de la ventana
    main_window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos