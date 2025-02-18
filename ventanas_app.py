import sys
import sqlite3
from PyQt5 import QtWidgets, QtCore, QtGui

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
        self.label.setText(_translate("page_v2", "Total: $"))
        self.label_2.setText(_translate("page_v2", "    0"))
        self.pushButton_3.setText(_translate("page_v2", "Borrar"))

# Clase principal de la aplicación para page_v2
class Ventana2Window(QtWidgets.QWidget, Ui_page_v2):
    def __init__(self, user_name):
        super().__init__()
        self.setupUi(self)  # Configura la interfaz gráfica
        self.user_active.setText(f"usuario activo: {user_name}")

        # Conectar el botón Helados a la función manejadora
        self.Helados.clicked.connect(self.on_helados_clicked)
        self.cono1_count = 0  # Contador para el botón 'cono 1'
        self.cono2_count = 0  # Contador para el botón 'cono 2'
        self.canasta2_count = 0  # Contador para el botón 'canasta 2'
        self.canasta3_count = 0  # Contador para el botón 'canasta 3'
        self.super_canasta_count = 0  # Contador para el botón 'super canasta'
        self.canasta_infantil_count = 0  # Contador para el botón 'canasta infantil'
        self.canasta_frutal_count = 0  # Contador para el botón 'canasta frutal'
        self.canasta_galette_count = 0  # Contador para el botón 'canasta galette'
        self.canasta_pow_ice_count = 0  # Contador para el botón 'canasta pow ice'
        self.total_price = 0  # Total price
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Product', 'Price', 'Cant'])
        self.tableView.setModel(self.model)

        # Conectar el botón Borrar a la función manejadora
        self.pushButton_3.clicked.connect(self.on_borrar_clicked)

    def on_helados_clicked(self):
        # boton 'cono 1'
        self.new_button1 = QtWidgets.QPushButton(self)
        self.new_button1.setGeometry(QtCore.QRect(260, 30, 91, 30))
        self.new_button1.setText("cono 1")
        self.new_button1.show()
        self.new_button1.clicked.connect(self.on_cono1_clicked)

        # botón 'cono 2'
        self.new_button2 = QtWidgets.QPushButton(self)
        self.new_button2.setGeometry(QtCore.QRect(260, 70, 91, 30))
        self.new_button2.setText("cono 2")
        self.new_button2.show()
        self.new_button2.clicked.connect(self.on_cono2_clicked)

        # botón 'canasta 2'
        self.new_button3 = QtWidgets.QPushButton(self)
        self.new_button3.setGeometry(QtCore.QRect(360, 30, 91, 30))
        self.new_button3.setText("canasta 2")
        self.new_button3.show()
        self.new_button3.clicked.connect(self.on_canasta2_clicked)

        # botón 'canasta 3'
        self.new_button4 = QtWidgets.QPushButton(self)
        self.new_button4.setGeometry(QtCore.QRect(360, 70, 91, 30))
        self.new_button4.setText("canasta 3")
        self.new_button4.show()
        self.new_button4.clicked.connect(self.on_canasta3_clicked)

        # botón 'super canasta'
        self.new_button5 = QtWidgets.QPushButton(self)
        self.new_button5.setGeometry(QtCore.QRect(360, 110, 91, 30))
        self.new_button5.setText("super canasta")
        self.new_button5.show()
        self.new_button5.clicked.connect(self.on_super_canasta_clicked)

        # botón 'canasta frutal'
        self.new_button6 = QtWidgets.QPushButton(self)
        self.new_button6.setGeometry(QtCore.QRect(360, 150, 91, 30))
        self.new_button6.setText("canasta frutal")
        self.new_button6.show()
        self.new_button6.clicked.connect(self.on_canasta_frutal_clicked)

        # botón 'canasta galette'
        self.new_button7 = QtWidgets.QPushButton(self)
        self.new_button7.setGeometry(QtCore.QRect(360, 190, 91, 30))
        self.new_button7.setText("canasta galette")
        self.new_button7.show()
        self.new_button7.clicked.connect(self.on_canasta_galette_clicked)

        # botón 'canasta pow ice'
        self.new_button8 = QtWidgets.QPushButton(self)
        self.new_button8.setGeometry(QtCore.QRect(360, 230, 91, 30))
        self.new_button8.setText("canasta pow ice") 
        self.new_button8.show()
        self.new_button8.clicked.connect(self.on_canasta_pow_ice_clicked)

        # botón 'canasta infantil'
        self.new_button9 = QtWidgets.QPushButton(self)
        self.new_button9.setGeometry(QtCore.QRect(360, 270, 91, 30))
        self.new_button9.setText("canasta infantil") 
        self.new_button9.show()
        self.new_button9.clicked.connect(self.on_canasta_infantil_clicked)

    def on_cono1_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'cono 1'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.cono1_count += 1
            self.total_price += price

            # Check if "cono 1" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "cono 1":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.cono1_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.cono1_count))])

            self.label_2.setText(str(self.total_price))

    def on_cono2_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'cono 2'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.cono2_count += 1
            self.total_price += price

            # Check if "cono 2" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "cono 2":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.cono2_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.cono2_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta2_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta 2'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta2_count += 1
            self.total_price += price

            # Check if "canasta 2" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta 2":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta2_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta2_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta3_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta 3'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta3_count += 1
            self.total_price += price

            # Check if "canasta 3" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta 3":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta3_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta3_count))])

            self.label_2.setText(str(self.total_price))

    def on_super_canasta_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'super canasta'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.super_canasta_count += 1
            self.total_price += price

            # Check if "super canasta" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "super canasta":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.super_canasta_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.super_canasta_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta_infantil_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta infantil'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta_infantil_count += 1
            self.total_price += price

            # Check if "canasta infantil" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta infantil":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta_infantil_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta_infantil_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta_frutal_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta frutal'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta_frutal_count += 1
            self.total_price += price

            # Check if "canasta frutal" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta frutal":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta_frutal_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta_frutal_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta_galette_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta galette'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta_galette_count += 1
            self.total_price += price

            # Check if "canasta galette" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta galette":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta_galette_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta_galette_count))])

            self.label_2.setText(str(self.total_price))

    def on_canasta_pow_ice_clicked(self):
        conn = sqlite3.connect('/home/andres/Documentos/App_pow_ice/databases/Pow_Ice')
        cursor = conn.cursor()
        cursor.execute("SELECT product, price FROM products WHERE product = 'canasta pow ice'")
        result = cursor.fetchone()
        conn.close()

        if result:
            product, price = result
            self.canasta_pow_ice_count += 1
            self.total_price += price

            # Check if "canasta pow ice" already exists in the table
            for row in range(self.model.rowCount()):
                if self.model.item(row, 0).text() == "canasta pow ice":
                    self.model.setItem(row, 2, QtGui.QStandardItem(str(self.canasta_pow_ice_count)))
                    break
            else:
                self.model.appendRow([QtGui.QStandardItem(product), QtGui.QStandardItem(str(price)), QtGui.QStandardItem(str(self.canasta_pow_ice_count))])

            self.label_2.setText(str(self.total_price))

    def on_borrar_clicked(self):
        if self.model.rowCount() > 0:
            last_row = self.model.rowCount() - 1
            product_item = self.model.item(last_row, 0)
            price_item = self.model.item(last_row, 1)
            cant_item = self.model.item(last_row, 2)
            if product_item and price_item and cant_item:
                product = product_item.text()
                price = float(price_item.text())
                cant = int(cant_item.text())
                self.total_price -= price * cant
                if self.total_price < 0:
                    self.total_price = 0
                self.label_2.setText(str(self.total_price))
                cant_item.setText("0")
                if product == "cono 1":
                    self.cono1_count = 0
                elif product == "cono 2":
                    self.cono2_count = 0
                elif product == "canasta 2":
                    self.canasta2_count = 0
                elif product == "canasta 3":
                    self.canasta3_count = 0
                elif product == "super canasta":
                    self.super_canasta_count = 0
                elif product == "canasta infantil":
                    self.canasta_infantil_count = 0
                elif product == "canasta frutal":
                    self.canasta_frutal_count = 0
                elif product == "canasta galette":
                    self.canasta_galette_count = 0
                elif product == "canasta pow ice":
                    self.canasta_pow_ice_count = 0
            self.model.removeRow(last_row)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # Crea la aplicación
    main_window = MainWindow()  # Crea una instancia de la ventana principal
    main_window.setGeometry(100, 100, 720, 480)  # Define la posición y tamaño de la ventana
    main_window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el bucle de eventos