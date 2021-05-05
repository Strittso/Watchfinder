from tkinter import *
from watchfinder import *
from watch import *

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


class FinderPage:

    def __init__(self, window):
        self.wf = Watchfinder()
        self.watches = self.wf.get_watches()

        self.finder_page = Frame(window.root)

        self.generate_categories_frame()

        self.watches_frame = Frame(self.finder_page)
        self.watches_row = 1
        for element in self.watches:
            watch = self.watches[element]
            watch.show_data(self.watches_frame, self.watches_row, 0)
            self.watches_row = self.watches_row + 1

        self.back_button = Button(self.watches_frame, text = "Back to Start", command = lambda: window.show_start_page())
        self.back_button.grid(row = 20, column = 0)
        self.label = Label(self.watches_frame, text = "Watches")
        self.label.grid(row = 0, column = 0)
        self.watches_frame.grid(row = 0, column = 1)

        self.finder_page.pack_forget()

    def show(self):
        self.finder_page.pack(expand = YES)

    def hide(self):
        self.finder_page.pack_forget()

        
############################################################################################
    def generate_categories_frame(self):
        self.categories_frame = Frame(self.finder_page)
        self.categories = self.wf.get_categories()

        self.label = Label(self.categories_frame, text = "Please select Categoies")
        self.label.grid(row = 0, column = 0, pady = 5)

        row_index = 1
        self.category_frames = {}
        self.option_frames = {}
        self.options_checkbuttons = {}
        self.option_vars = {}
        for category in self.categories:
            self.category_frames[category] = Frame(self.categories_frame)
            category_lb = Label(self.category_frames[category], text = category)
            category_lb.grid(row = 0, column = 0)


            self.option_frames[category] = Frame(self.category_frames[category])
            options = self.wf.get_options(category)
            
            
            option_index = 0
            for option in options:
                self.option_vars[option] = IntVar()
                self.options_checkbuttons[option] = Checkbutton(self.option_frames[category], text = option, variable = self.option_vars[option])
                self.options_checkbuttons[option].grid(row = option_index, column = 0)
                option_index = option_index + 1

            self.option_frames[category].grid(row = 1, column = 0)
            
            self.category_frames[category].grid(row = row_index, column = 0, pady = 5)
            row_index = row_index + 1

        

        self.search_button = Button(self.categories_frame, text = "Search")
        self.search_button.grid(row = 19, column = 0, pady = 5)

        self.categories_frame.grid(row = 0, column = 0)
        

        return self.categories_frame

    def refresh_page(self):
        self.watches_row = 1
        for element in self.watches:
            watch = self.watches[element]
            watch.show_data(self.watches_frame, self.watches_row, 0)
            self.watches_row = self.watches_row + 1

