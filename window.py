from tkinter import *
from pages.startpage import *
from pages.addDataPage import *
from pages.finderpage import *


background_color = "orange"

class Window:

    def __init__(self, bcolor):
        self.root = Tk()
        self.root.title('Watchfinder')
        self.root.state('zoomed')
        self.root.config(background = bcolor)

        self.start_page = StartPage(self)
        self.add_data_page = AddDataPage(self)
        self.finder_page = FinderPage(self)
        self.root.mainloop()

    def show_add_data_page(self):
        self.start_page.hide()
        self.add_data_page.show()

    def show_finder_page(self):
        self.finder_page.show()
        self.start_page.hide()  
    
    def show_start_page(self):
        self.start_page.show()
        self.finder_page.hide()
        self.add_data_page.hide()


w = Window(background_color)
        
        
        
      
