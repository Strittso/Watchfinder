from tkinter import *
from watchfinder import *



class FinderPage:

    def __init__(self, window):
        self.finder_page = Frame(window.root)

        """Categories: brand, size, price, Antrieb (Quarz, Automatik, Handaufzug), Stil (sportlich, klassisch),
           Komplikation (z.B. Datumanzeige), Geschlecht, Zifferblattfarbe, Bandmaterial"""
        """self.categories_frame = Frame(self.finder_page)"""
        

        #brand 
        """self.brand_lb = Label(self.categories_frame, text = "Brand")
        self.brand_lb.grid(row = 1, column = 0, pady = 5)
        self.brand_frame = Frame(self.categories_frame)
        self.var_iwc = IntVar()
        self.iwc_checkbox = Checkbutton(self.brand_frame, variable = self.var_iwc)
        self.iwc_checkbox.grid(row = 0, column = 0)
        self.iwc_label = Label(self.brand_frame, text = "IWC")
        self.iwc_label.grid(row = 0, column = 1)
        self.brand_frame.grid(row = 2, column = 0, pady = 5)"""

        self.generate_categories_frame()
        

        
        

        self.watches_frame = Frame(self.finder_page)
        self.back_button = Button(self.watches_frame, text = "Back to Start", command = lambda: window.show_start_page())
        self.back_button.grid(row = 1, column = 0)
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

        self.wf = Watchfinder()
        self.watches = self.wf.get_watches()
        print(self.watches)

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


