import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import MainWindowKursacha
import drivers
import maintenance
import accidents
import vehicles
import fuel
import trips
import inspections
import login 
import os



class Expample(QtWidgets.QMainWindow, MainWindowKursacha.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Login(QtWidgets.QMainWindow, login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        self.login=self.lineEdit.text()
        self.passwod=self.lineEdit_2.text()

        if self.login == "Administrator" and self.passwod == "Administrator":
            self.example = MainWindow()
            self.example.show()
            self.close()
        
        else:
             QtWidgets.QMessageBox.warning(self, "Ошибка", "Неправильный логин или пароль")



class Accidents(QtWidgets.QMainWindow, accidents.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_accidents)
        self.Dell.clicked.connect(self.delete_accident)
        self.Add.clicked.connect(self.add_accident)
        self.Sort.clicked.connect(self.sort_accidents)
        self.Change.clicked.connect(self.update_accident)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_accidents(self):
        connection, cursor = self.establish_connection()
        cursor.execute('SELECT * FROM "Accidents"')
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def delete_accident(self):
        accident_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Accidents WHERE accident_id = ?", (accident_id,))
        connection.commit()
        connection.close()

    def add_accident(self):
        vehicle_id = self.AddLine.text()
        driver_id = self.AddLine_1.text()
        date = self.AddLine_2.text()
        location = self.AddLine_3.text()
        description = self.AddLine_4.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Accidents (vehicle_id, driver_id, date, location, description) VALUES(?,?,?,?,?)",
                       (vehicle_id, driver_id, date, location, description))
        connection.commit()
        connection.close()

    def sort_accidents(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Accidents ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def update_accident(self):
        connection, cursor = self.establish_connection()
        cursor.execute(f"UPDATE Accidents SET vehicle_id='{self.ChangeLine_1.text()}', driver_id='{self.ChangeLine_2.text()}', date='{self.ChangeLine_3.text()}', location='{self.ChangeLine_4.text()}', description='{self.ChangeLine_5.text()}' WHERE accident_id='{self.ChangeLine.text()}'")
        connection.commit()
        connection.close()

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3
import drivers

class Drivers(QtWidgets.QMainWindow, drivers.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.load_drivers)
        self.Dell.clicked.connect(self.delete_driver)
        self.Add.clicked.connect(self.add_driver)
        self.Sort.clicked.connect(self.sort_drivers)
        self.Change.clicked.connect(self.update_driver)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_drivers(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Drivers'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def delete_driver(self):
        driver_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Drivers WHERE driver_id =?", (driver_id,))
        connection.commit()
        connection.close()

    def add_driver(self):
        first_name = self.AddLine.text()
        last_name = self.AddLine_1.text()
        email = self.AddLine_2.text()
        phone_number = self.AddLine_3.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO 'Drivers' ('first_name', 'last_name', 'email', 'phone_number') VALUES (?, ?, ?, ?)",
                       (first_name, last_name, email, phone_number))
        connection.commit()
        connection.close()

    def sort_drivers(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM 'Drivers' ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def update_driver(self):
        connection, cursor = self.establish_connection()
        cursor.execute(f"UPDATE 'Drivers' SET first_name='{self.ChangeLine_1.text()}', last_name='{self.ChangeLine_2.text()}', email='{self.ChangeLine_3.text()}', phone_number='{self.ChangeLine_4.text()}' WHERE driver_id='{self.ChangeLine.text()}'")
        connection.commit()
        connection.close()


class Fuel(QtWidgets.QMainWindow, fuel.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_fuel)
        self.Dell.clicked.connect(self.delete_fuel)
        self.Add.clicked.connect(self.add_fuel)
        self.Sort.clicked.connect(self.sort_fuel)
        self.Change.clicked.connect(self.update_fuel)
        

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_fuel(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Fuel'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def delete_fuel(self):
        fuel_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Fuel WHERE fuel_id =?", (fuel_id,))
        connection.commit()
        connection.close()

    def add_fuel(self):
        vehicle_id = self.AddLine.text()
        fuel_type = self.AddLine_1.text()
        fuel_date = self.AddLine_2.text()
        fuel_quantity = self.AddLine_3.text()
        fuel_cost = self.AddLine_4.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Fuel (vehicle_id, fuel_type, fuel_date, fuel_quantity, fuel_cost) VALUES (?, ?, ?, ?, ?)",
                       (vehicle_id, fuel_type, fuel_date, fuel_quantity, fuel_cost))
        connection.commit()
        connection.close()

    def sort_fuel(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Fuel ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def update_fuel(self):
        connection, cursor = self.establish_connection()
        cursor.execute(f"UPDATE Fuel SET vehicle_id='{self.ChangeLine_1.text()}', fuel_type='{self.ChangeLine_2.text()}', fuel_date='{self.ChangeLine_3.text()}', fuel_quantity='{self.ChangeLine_4.text()}', fuel_cost='{self.ChangeLine_5.text()}' WHERE fuel_id='{self.ChangeLine.text()}'")
        connection.commit()
        connection.close()


class Inspection(QtWidgets.QMainWindow, inspections.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_inspection)
        self.Dell.clicked.connect(self.delete_inspection)
        self.Sort.clicked.connect(self.sort_inspection)
        self.Add.clicked.connect(self.add_inspection)
        self.Change.clicked.connect(self.update_inspection)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_inspection(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Inspections'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def delete_inspection(self):
        inspection_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Inspections WHERE inspection_id =?", (inspection_id,))
        connection.commit()
        connection.close()

    def sort_inspection(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Inspections ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def add_inspection(self):
        vehicle_id = self.AddLine.text()
        inspection_type = self.AddLine_1.text()
        inspection_date = self.AddLine_2.text()
        inspection_result = self.AddLine_3.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Inspections (vehicle_id, inspection_type, inspection_date, inspection_result) VALUES (?, ?, ?, ?)",
                       (vehicle_id, inspection_type, inspection_date, inspection_result))
        connection.commit()
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def update_inspection(self):
        connection, cursor = self.establish_connection()
        cursor.execute(f"UPDATE Inspections SET vehicle_id='{self.ChangeLine_1.text()}', inspection_type='{self.ChangeLine_2.text()}', inspection_date='{self.ChangeLine_3.text()}', inspection_result='{self.ChangeLine_4.text()}' WHERE inspection_id='{self.ChangeLine.text()}'")
        connection.commit()
        connection.close()

class Mainstance(QtWidgets.QMainWindow, maintenance.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_mainstance)
        self.Add.clicked.connect(self.add_mainstance)
        self.Dell.clicked.connect(self.delete_mainstance)
        self.Sort.clicked.connect(self.sort_mainstance)
        self.Change.clicked.connect(self.update_mainstance)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_mainstance(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Maintenance'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def add_mainstance(self):
        vehicle_id = self.AddLine.text()
        maintenance_type = self.AddLine_1.text()
        maintenance_date = self.AddLine_2.text()
        maintenance_cost = self.AddLine_3.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Maintenance (vehicle_id, maintenance_type, maintenance_date, maintenance_cost) VALUES (?, ?, ?, ?)",
                       (vehicle_id, maintenance_type, maintenance_date, maintenance_cost))
        connection.commit()
        connection.close()

    def delete_mainstance(self):
        maintenance_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Maintenance WHERE maintenance_id =?", (maintenance_id,))
        connection.commit()
        connection.close()

    def sort_mainstance(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Maintenance ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)

    def update_mainstance(self):
        connection, cursor = self.establish_connection()
        cursor.execute(f"UPDATE Maintenance SET vehicle_id='{self.ChangeLine_1.text()}', maintenance_type='{self.ChangeLine_2.text()}', maintenance_date='{self.ChangeLine_3.text()}', maintenance_cost='{self.ChangeLine_4.text()}' WHERE maintenance_id='{self.ChangeLine.text()}'")
        connection.commit()
        connection.close()




class Trips(QtWidgets.QMainWindow, trips.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_trips)
        self.Add.clicked.connect(self.add_trip)
        self.Dell.clicked.connect(self.delete_trip)
        self.Change.clicked.connect(self.update_trip)
        self.Sort.clicked.connect(self.sort_trips)

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_trips(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Trips'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()
    
    def add_trip(self):
        vehicle_id = self.AddLine.text()
        driver_id = self.AddLine_1.text()
        start_date = self.AddLine_2.text()
        end_date = self.AddLine_3.text()
        start_location = self.AddLine_4.text()
        end_location = self.AddLine_5.text()
        trip_purpose = self.AddLine_6.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Trips (vehicle_id, driver_id, start_date, end_date, start_location, end_location, trip_purpose) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (vehicle_id, driver_id, start_date, end_date, start_location, end_location, trip_purpose))
        connection.commit()
        connection.close()
    
    def delete_trip(self):
        trip_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Trips WHERE trip_id =?", (trip_id,))
        connection.commit()
        connection.close()

    def update_trip(self):
        trip_id = self.ChangeLine.text()
        vehicle_id = self.ChangeLine_1.text()
        driver_id = self.ChangeLine_2.text()
        start_date = self.ChangeLine_3.text()
        end_date = self.ChangeLine_4.text()
        start_location = self.ChangeLine_5.text()
        end_location = self.ChangeLine_6.text()
        trip_purpose = self.ChangeLine_7.text()
        connection, cursor = self.establish_connection()
        cursor.execute("UPDATE Trips SET vehicle_id=?, driver_id=?, start_date=?, end_date=?, start_location=?, end_location=?, trip_purpose=? WHERE trip_id=?",
                       (vehicle_id, driver_id, start_date, end_date, start_location, end_location, trip_purpose, trip_id))
        connection.commit()
        connection.close()

    def sort_trips(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Trips ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)


class Vehicles(QtWidgets.QMainWindow, vehicles.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.load_vehicles)
        self.Dell.clicked.connect(self.delete_vehicle)
        self.Add.clicked.connect(self.add_vehicle)
        self.Sort.clicked.connect(self.sort_vehicles)
        self.Change.clicked.connect(self.update_vehicle)
        

    def establish_connection(self):
        connection = sqlite3.connect(r"C:\Users\lovea\OneDrive\Рабочий стол\KursachDb-main\qwe\transport.db")
        cursor = connection.cursor()
        return connection, cursor

    def load_vehicles(self):
        connection, cursor = self.establish_connection()
        cursor.execute("SELECT * FROM 'Vehicles'")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def delete_vehicle(self):
        vehicle_id = self.DellLine.text()
        connection, cursor = self.establish_connection()
        cursor.execute("DELETE FROM Vehicles WHERE vehicle_id =?", (vehicle_id,))
        connection.commit()
        connection.close()

    def add_vehicle(self):
        make = self.AddLine.text()
        model = self.AddLine_1.text()
        year = self.AddLine_2.text()
        license_plate = self.AddLine_3.text()
        owner_id = self.AddLine_4.text()
        connection, cursor = self.establish_connection()
        cursor.execute("INSERT INTO Vehicles (make, model, year, license_plate, owner_id) VALUES (?, ?, ?, ?, ?)",
                       (make, model, year, license_plate, owner_id))
        connection.commit()
        connection.close()

    def sort_vehicles(self):
        sort_column = self.lineEdit_13.text()
        connection, cursor = self.establish_connection()
        cursor.execute(f"SELECT * FROM Vehicles ORDER BY {sort_column}")
        rows = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        self.display_table_data(column_names, rows)
        connection.close()

    def update_vehicle(self):
        vehicle_id = self.ChangeLine.text()
        make = self.ChangeLine_1.text()
        model = self.ChangeLine_2.text()
        year = self.ChangeLine_3.text()
        license_plate = self.ChangeLine_4.text()
        owner_id = self.ChangeLine_5.text()
        connection, cursor = self.establish_connection()
        cursor.execute("UPDATE Vehicles SET make=?, model=?, year=?, license_plate=?, owner_id=? WHERE vehicle_id=?",
                       (make, model, year, license_plate, owner_id, vehicle_id))
        connection.commit()
        connection.close()

    def display_table_data(self, column_names, rows):
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i + 1, j, item)




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.accidents = Accidents()
        self.drivers = Drivers()
        self.fuel = Fuel()
        self.inspection = Inspection()
        self.maintenance = Mainstance()
        self.trips = Trips()
        self.vehicles = Vehicles()
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.drivers)
        self.stacked_widget.addWidget(self.fuel)
        self.stacked_widget.addWidget(self.inspection)
        self.stacked_widget.addWidget(self.maintenance)
        self.stacked_widget.addWidget(self.trips)
        self.stacked_widget.addWidget(self.vehicles)
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.accidents.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_drivers)
        self.drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.fuel.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)
        self.example.MaintenanceBtn.clicked.connect(self.show_maintenance)
        self.maintenance.Back.clicked.connect(self.show_example)
        self.example.TripsBtn.clicked.connect(self.show_trips)
        self.trips.Back.clicked.connect(self.show_example)
        self.example.Vehicles.clicked.connect(self.show_vehicles)
        self.vehicles.Back.clicked.connect(self.show_example)
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_drivers(self):
        self.stacked_widget.setCurrentWidget(self.drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.fuel)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    
    def show_maintenance(self):
        self.stacked_widget.setCurrentWidget(self.maintenance)

    def show_trips(self):
        self.stacked_widget.setCurrentWidget(self.trips)

    def show_vehicles(self):
        self.stacked_widget.setCurrentWidget(self.vehicles)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec_())
