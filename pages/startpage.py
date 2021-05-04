from tkinter import *

class StartPage:


    def __init__(self, window):
        self.start_page = Frame(window.root)
        self.start_page.config(background = "orange")
        self.label = Label(self.start_page, text = "Welcome to the Watchfinder", font = "30")
        self.label.grid(row = 0, column = 0, pady = 5)
        self.add_data_button = Button(self.start_page, text = "Add new Watches to Database", command = lambda: window.show_add_data_page())
        self.add_data_button.grid(row = 1, column = 0, pady = 5)
        self.finder_button = Button(self.start_page, text = "Start Watchfinder",command = lambda: window.show_finder_page())
        self.finder_button.grid(row = 2, column = 0, pady = 5)
        self.start_page.pack(expand = YES)

    def hide(self):
        self.start_page.pack_forget()

    def show(self):
        self.start_page.pack(expand = YES)