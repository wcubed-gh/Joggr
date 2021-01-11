from PyQt5.QtWidgets import QAction, QApplication, QLabel, QMainWindow, QMenu, QTableWidget, QVBoxLayout, QWidget
import sqlite3 as sl
from sys import exit

#Declare variables
db_name = str('example.db')

#Main function
def main():
    cursor = db_init()
    app = QApplication([])
    window = Window()
    app.exec()


#Database init function
def db_init():
    try:
        db_connection = sl.connect(db_name)
        cursor = db_connection.cursor()
    except:
        cursor = None
        exit("Something went wrong connecting to the database. Exiting.")
    try:
        cursor.execute('create table if not exists joggr (name text, url text, last_visited text, tags text)')
        return cursor
    except:
        exit("Something went wrong creating the database. Exiting")

def db_add_bookmark(cursor, entry):
    try:
        cursor.execute("insert into joggr values(?)",entry)
    except:
        pass

def db_remove_bookmark(cursor, entry):
    print()
def db_modify_bookmark(cursor, old_entry, new_entry):
    print()
#Generates and draws Qt window
class Window(QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle("Joggr")
        self.setGeometry(0,0,480,270)
        self.menu_bar()
        self.show()

    #Create and populate the menu bar
    def menu_bar(self):
        menu_bar = self.menuBar()
        #File Menu
        file_menu = QMenu("&File",self)
        menu_bar.addMenu(file_menu)
        file_import = QAction("&File", self)
        file_export = QAction("&Export", self)
        file_save = QAction("&Save", self)
        file_save_as = QAction("Save &As", self)
        file_exit = QAction("&Exit", self)
        file_actions = [file_import, file_export, file_save, file_save_as, file_exit]
        file_menu.addActions(file_actions)
        #Edit Menu
        edit_menu = QMenu("&Edit", self)
        menu_bar.addMenu(edit_menu)
        edit_new = QAction("&New Bookmark", self)
        edit_edit = QAction("&Edit Bookmark", self)
        edit_delete = QAction("&Delete Bookmark", self)
        edit_actions = [edit_new, edit_edit, edit_delete]
        edit_menu.addActions(edit_actions)
        #Help Menu
        help_menu = QMenu("&Help", self)
        menu_bar.addMenu(help_menu)
        help_feedback = QAction("&Feedback", self)
        help_about = QAction("&About", self)
        help_actions = [help_feedback, help_about]
        help_menu.addActions(help_actions)
        #Show menu bar
        self.setMenuBar(menu_bar)


#Executes main function
main()
