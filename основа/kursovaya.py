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



class Expample(QtWidgets.QMainWindow, MainWindowKursacha.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        



class Accidents(QtWidgets.QMainWindow,accidents.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        self.Sort.clicked.connect(self.SortAccidents)
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect("transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Accidents'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Accidents WHERE accident_id = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Accidents (vehicle_id,driver_id,date,location,description) VALUES(?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),))
        self.connection.commit()
        self.connection.close()

    def SortAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Accidents ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Accidents SET vehicle_id='{self.ChangeLine_1.text()}', driver_id='{self.ChangeLine_2.text()}', date='{self.ChangeLine_3.text()}', location='{self.ChangeLine_4.text()}', description='{self.ChangeLine_5.text()}' WHERE accident_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()

class Drivers(QtWidgets.QMainWindow,drivers.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)
        self.Sort.clicked.connect(self.SortDrivers) 
        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Drivers'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Drivers WHERE driver_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Drivers' ('first_name', 'last_name', 'email', 'phone_number') VALUES (?, ?, ?, ?)",
                       (self.AddLine.text(), self.AddLine_1.text(), self.AddLine_2.text(), self.AddLine_3.text()))
                           
        self.connection.commit()
        self.connection.close()

    def SortDrivers(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Drivers' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()
        
        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    def ChangeDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Drivers' SET first_name='{self.ChangeLine_1.text()}', last_name='{self.ChangeLine_2.text()}', email='{self.ChangeLine_3.text()}', phone_number='{self.ChangeLine_4.text()}' WHERE driver_id='{self.ChangeLine.text()}'")
        
        self.connection.commit()
        self.connection.close()

class Fuel(QtWidgets.QMainWindow,fuel.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)
        self.Sort.clicked.connect(self.SortFuel)
        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Fuel'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Fuel WHERE fuel_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Fuel (vehicle_id,fuel_type,fuel_date,fuel_quantity,fuel_cost) VALUES(?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),))
        self.connection.commit()
        self.connection.close()

    def SortFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Fuel ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Fuel SET vehicle_id='{self.ChangeLine_1.text()}', fuel_type='{self.ChangeLine_2.text()}', fuel_date='{self.ChangeLine_3.text()}', fuel_quantity='{self.ChangeLine_4.text()}', fuel_cost='{self.ChangeLine_5.text()}' WHERE fuel_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Inspection(QtWidgets.QMainWindow,inspections.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Sort.clicked.connect(self.SortInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Inspections'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Inspections WHERE inspection_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def SortInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Inspections ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def AddInspection(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Inspections (vehicle_id,inspection_type,inspection_date,inspection_result) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Inspections SET vehicle_id='{self.ChangeLine_1.text()}', inspection_type='{self.ChangeLine_2.text()}', inspection_date='{self.ChangeLine_3.text()}', inspection_result='{self.ChangeLine_4.text()}' WHERE inspection_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Mainstance(QtWidgets.QMainWindow,maintenance.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Add.clicked.connect(self.MainstanceAdd)
        self.Dell.clicked.connect(self.DellMainstance)
        self.Sort.clicked.connect(self.SortMainstance)
        self.Change.clicked.connect(self.ChangeMainstance)


    def test1(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Maintenance'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def MainstanceAdd(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Maintenance (vehicle_id,maintenance_type,maintenance_date,maintenance_cost) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def DellMainstance(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Maintenance WHERE maintenance_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def SortMainstance(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Maintenance ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeMainstance(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Maintenance SET vehicle_id='{self.ChangeLine_1.text()}', maintenance_type='{self.ChangeLine_2.text()}', maintenance_date='{self.ChangeLine_3.text()}', maintenance_cost='{self.ChangeLine_4.text()}' WHERE maintenance_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()




class Trips(QtWidgets.QMainWindow,trips.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Add.clicked.connect(self.TripsAdd)
        self.Dell.clicked.connect(self.DellTrips)
        self.Change.clicked.connect(self.ChangeTrips)
        self.Sort.clicked.connect(self.SortTrips)

    def test1(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Trips'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def TripsAdd(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Trips (vehicle_id,driver_id,start_date,end_date,start_location,end_location,trip_purpose) VALUES(?,?,?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text(),self.AddLine_6.text(),))
        self.connection.commit()
        self.connection.close()
    
    def DellTrips(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Trips WHERE trip_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def ChangeTrips(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Trips SET vehicle_id='{self.ChangeLine_1.text()}', driver_id='{self.ChangeLine_2.text()}', start_date='{self.ChangeLine_3.text()}', end_date='{self.ChangeLine_4.text()}', start_location ='{self.ChangeLine_5.text()}', end_location='{self.ChangeLine_6.text()}', trip_purpose='{self.ChangeLine_7.text()}' WHERE trip_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()

    def SortTrips(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Trips ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()


class Vehicles(QtWidgets.QMainWindow,vehicles.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)
        self.Sort.clicked.connect(self.SortFuel)
        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Vehicles'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM Vehicles WHERE vehicle_id =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO Vehicles (make,model,year,license_plate,owner_id) VALUES(?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),))
        self.connection.commit()
        self.connection.close()

    def SortFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM Vehicles ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\lovea\\OneDrive\\Документы\\my_project\\курсач\\transport.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE Vehicles SET make='{self.ChangeLine_1.text()}', model='{self.ChangeLine_2.text()}', year='{self.ChangeLine_3.text()}', license_plate='{self.ChangeLine_4.text()}', owner_id='{self.ChangeLine_5.text()}' WHERE vehicle_id='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()




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
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
