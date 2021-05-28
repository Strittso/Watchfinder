from tkinter import *
from pages import *


background_color = "orange"

class Window:
    """Class for the window. It already creates the Frames for the different pages as objekts of the classes for the pages. In the beginning
    only the startpage is visible. 
    The class has three Methods show_start_page, show_add_data_page() and show_finder_page() to show a several page and hide the others when
    you click on the corresponding buttons."""
    def __init__(self, bcolor):
        self.root = Tk()
        self.root.title('Watchfinder')
        self.root.state('zoomed')
        self.root.config(background = bcolor)
        #self.root.resizable(0,0)

        self.root_width = self.root.winfo_vrootwidth()
        self.root_height = self.root.winfo_vrootheight()

        self.start_page = StartPage(self, bcolor)
        self.add_data_page = AddDataPage(self, bcolor)
        self.finder_page = FinderPage(self, bcolor)
        self.root.mainloop()

    def show_add_data_page(self):
        self.start_page.hide()
        self.add_data_page.show()

    def show_finder_page(self):
        self.finder_page.show()
        self.start_page.hide()  
        self.finder_page.refresh_page()
    
    def show_start_page(self):
        self.start_page.show()
        self.finder_page.hide()
        self.add_data_page.hide()


w = Window(background_color)
        
        
        
      
