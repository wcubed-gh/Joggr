from PyQt5.QtWidgets import QApplication, QLabel, QTableWidget, QVBoxLayout, QWidget
import sqlite3 as sl

#Declare variables
db_name = str('example.db')

#Main function
def main():
    db_init()
    make_window()

#Database init function
def db_init():
    db_connection = sl.connect(db_name)
    cursor = db_connection.cursor()
    cursor.execute('create table if not exists joggr (name text, url text, last_visited text, tags text)')

#Generates and draws Qt window
def make_window():
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QTableWidget(3,3))
    window.setLayout(layout)
    window.show()
    app.exec_()

#Executes main function
main()
