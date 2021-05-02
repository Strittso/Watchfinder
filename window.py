from tkinter import *


background_color = "orange"

class Window:

    def __init__(self, bcolor):
        self.root = Tk()
        self.root.title('Watchfinder')
        self.root.state('zoomed')
        self.root.config(background = bcolor)

        self.start_page = StartPage(self)
        
        self.add_data_page = Frame(self.root)
        self.add_data_page.config(background = "red")
        self.label = Label(self.add_data_page, text = "Welcome to the Watchfinder")
        self.label.grid(row = 0, column = 0, pady = 5)
        self.button = Button(self.add_data_page, text = "Add new Watches to Database")
        self.button.grid(row = 1, column = 0, pady = 5)
        self.add_data_page.pack_forget()

        self.finder_page = Frame(self.root)
        self.label = Label(self.finder_page, text = "Please select Categoies")
        self.label.grid(row = 0, column = 0, pady = 5)
        self.button = Button(self.finder_page, text = "Add new Watches to Database")
        self.button.grid(row = 1, column = 0, pady = 5)
        self.finder_page.pack_forget()

        self.root.mainloop()

    def show_add_data_page(self):
        self.start_page.hide()
        self.add_data_page.pack(expand = YES)

    def show_finder_page(self):
        self.finder_page.pack(expand = YES)
        self.start_page.hide()  

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

w = Window(background_color)
        
        
        
      
