from tkinter import *

class Watch:
    """Attributes of Watch are all categaories taken in the database. For initialization you already need the data from the database.
    The class has the following Methods:
    -> get_data() to return all data of the watch as a dictionary; the category is the key, the option(s) is (/are) the values"""
    def __init__(self, watchdata):
        self.watchdata = watchdata
        self.brand = watchdata["Brand"]
        self.size = watchdata["Size(in mm)"]

    def get_data(self):
        """returns data of the watch as a dictionary: {"category":"option(s)"}"""
        return self.watchdata

    def show_data(self, master, row_index, column_index):
        """shows the data in the window on the finder page"""
        self.frame = Frame(master, bg = "black", bd = 2)

        self.watch_frame = Frame(self.frame)
        
        index = 1
        for element in self.watchdata:
            label_category = Label(self.watch_frame, text = element)
            label_category.grid(row = index, column = 0)
            label_values = Label(self.watch_frame, text = self.watchdata[element])
            label_values.grid(row = index, column = 1)
            index = index + 1
        self.watch_frame.pack()
        self.frame.grid(row = row_index, column = column_index, padx = 5, pady = 5)
            


