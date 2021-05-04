from tkinter import *

class AddDataPage:

    def __init__(self, window):
        self.add_data_page = Frame(window.root)
        self.add_data_page.config(background = "red")
        self.label = Label(self.add_data_page, text = "Welcome to the Watchfinder")
        self.label.grid(row = 0, column = 0, pady = 5)
        self.button = Button(self.add_data_page, text = "Add new Watches to Database")
        self.button.grid(row = 1, column = 0, pady = 5)
        self.back_button = Button(self.add_data_page, text = "Back to Start", command = lambda: window.show_start_page())
        self.back_button.grid(row = 2, column = 0, pady = 5)
        self.add_data_page.pack_forget()

    def show(self):
        self.add_data_page.pack(expand = YES)
    
    def hide(self):
        self.add_data_page.pack_forget()