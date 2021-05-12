from tkinter import *
from tkinter import filedialog
from watchfinder import *
from watch import *
from analogClock import *
from PIL import Image, ImageTk

class StartPage:
    """Class creates the Startpage as a frame with Welcome label, buttons to get to the other two pages and also an analog clock which shows the current
    time in hours, minutes and seconds. It has functions to show and hide the Frame."""

    def __init__(self, window, bcolor):
        self.start_page = Frame(window.root)
        self.start_page.config(background = bcolor)

        self.text_frame = Frame(self.start_page, background = bcolor)
        self.label = Label(self.text_frame, text = "Welcome to the Watchfinder", font = "30", bg = bcolor)
        self.label.grid(row = 0, column = 0, pady = 5)
        self.add_data_button = Button(self.text_frame, text = "Add new Watches to Database", command = lambda: window.show_add_data_page())
        self.add_data_button.grid(row = 1, column = 0, pady = 5)
        self.finder_button = Button(self.text_frame, text = "Start Watchfinder",command = lambda: window.show_finder_page())
        self.finder_button.grid(row = 2, column = 0, pady = 5)
        self.text_frame.pack(expand = YES, side = LEFT)

        self.clock_frame = Frame(self.start_page, background = bcolor)
        self.clock = AnalogClock(self, bcolor)
        self.clock_frame.pack(expand = YES, side = LEFT)

        self.start_page.pack(expand = YES)

    def hide(self):
        self.start_page.pack_forget()

    def show(self):
        self.start_page.pack(expand = YES)


class AddDataPage:
    """Class AddDataPage creates the Add Data Page, where you can add new watches to the database."""

    def __init__(self, window, bcolor):
        self.add_data_page = Frame(window.root)
        self.add_data_page.config(background = bcolor)
       
        self.back_button = Button(self.add_data_page, text = "Back to Start", command = lambda: window.show_start_page())
        self.back_button.grid(row = 2, column = 0, pady = 5)

        self.add_data_page.pack_forget()

    def show(self):
        self.add_data_page.pack(expand = YES)
    
    def hide(self):
        self.add_data_page.pack_forget()

    def open_watch_image(self):
        filepath = filedialog.askopenfilename()
        file = Image.open(filepath)
        watch_image = ImageTk.PhotoImage(file)
        self.canvas.create_image(300,300, image = watch_image)
        self.canvas.image = watch_image
        file.save("./testfolder/IWtest.jpg")

    def generate_add_frame(self):
        self.add_frame = Frame(self.add_data_page)

        self.canvas = Canvas(self.add_frame, width = 300, height = 300)
        self.canvas.grid(row = 0, column = 0, pady = 5, padx = 5)
        self.image_button = Button(self.add_frame, text = "Select Picture", command = lambda: self.open_watch_image())
        self.image_button.grid(row = 1)




class FinderPage:

    def __init__(self, window, bcolor):
        self.window = window
        self.bcolor = bcolor
        self.wf = Watchfinder()
        self.watches = self.wf.get_watches()

        self.finder_page = Frame(self.window.root, bg = self.bcolor)        

        self.generate_categories_frame()

        self.watches_frame_width = (0.8*self.window.root_width)
        self.frame_wf = Frame(self.finder_page, bg = bcolor)
        self.frame_wf.place(x = self.cf_width, y = 0, width = self.watches_frame_width, height = self.window.root_height)
        self.canvas_wf = Canvas(self.frame_wf, bg = "orange")
        self.frame_wf_out = Frame(self.canvas_wf, bg = self.bcolor)
        self.watches_frame = Frame(self.finder_page, bg = self.bcolor)
        self.scrollbar_wf = Scrollbar(self.frame_wf, orient = "vertical", command = self.canvas_wf.yview)
        self.refresh_page()

        
        self.finder_page.pack_forget()

    def show(self):
        self.finder_page.pack(expand = YES, fill = BOTH)

    def hide(self):
        self.finder_page.pack_forget()

    def generate_categories_frame(self):
        self.cf_width = (0.2*self.window.root_width)
        self.frame_cf = Frame(self.finder_page, bg = self.bcolor)
        self.frame_cf.place(x = 0, y = 0, width = self.cf_width, height = self.window.root_height)
        self.canvas_cf = Canvas(self.frame_cf, bg = "orange")

        self.frame_cf_out = Frame(self.canvas_cf, bg = self.bcolor)
        self.categories_frame = Frame(self.frame_cf_out, bg = self.bcolor)
        self.categories_frame.grid(row = 0, column = 0)
        self.categories = self.wf.get_categories()

        self.label = Label(self.categories_frame, text = "Please select Categoies", bg = self.bcolor, font = "30")
        self.label.grid(row = 0, column = 0, pady = 30, padx = 30, sticky = W)

        row_index = 1
        self.category_frames = {}
        self.option_frames = {}
        self.options_checkbuttons = {}
        self.category_option_vars = {}
        for category in self.categories:
            self.category_frames[category] = Frame(self.categories_frame, bg = self.bcolor)
            category_lb = Label(self.category_frames[category], text = category, bg = self.bcolor)
            category_lb.grid(row = 0, column = 0, sticky = W)


            self.option_frames[category] = Frame(self.category_frames[category], bg = self.bcolor)
            options = self.wf.get_options(category)
            
            option_vars = {}
            option_index = 0
            for option in options:
                option_vars[option] = IntVar()
                self.options_checkbuttons[option] = Checkbutton(self.option_frames[category], text = option, variable = option_vars[option], bg = self.bcolor)
                self.options_checkbuttons[option].grid(row = option_index, column = 0, sticky = W)
                option_index = option_index + 1

            self.category_option_vars[category] = option_vars 
            self.option_frames[category].grid(row = 1, column = 0, sticky = W)
            
            self.category_frames[category].grid(row = row_index, column = 0, padx = 30, pady = 5, sticky = W)
            row_index = row_index + 1

        self.search_button = Button(self.categories_frame, text = "Search", command = lambda: self.refresh_page())
        self.search_button.grid(row = row_index, column = 0, pady = 5)
      
        # to get the height of a frame just works when every widget is placed and only after Frame.update()
        self.scrollbar_cf = Scrollbar(self.frame_cf, orient = "vertical", command = self.canvas_cf.yview)

        self.categories_frame.update()
        self.cf_height = self.categories_frame.winfo_height()
        self.frame_cf_out.config(height = (self.cf_height + 100))
        #part has to be after the configuration (height) of the frame, otherwise it doesn't work
        self.canvas_cf.configure(yscrollcommand = self.scrollbar_cf.set)
        self.scrollbar_cf.pack(side = RIGHT, fill = Y)
        self.canvas_cf.pack(side = "left")
        self.canvas_cf.create_window((0,0), window = self.frame_cf_out, anchor = "nw")
        self.frame_cf_out.bind("<Configure>", self.canvas_cf.configure(scrollregion = self.canvas_cf.bbox("all"), width = (self.cf_width-20), height = self.window.root_height ))


    def refresh_page(self):
        #Funktion oben integrieren, bzw so dass button nicht gdelöscht wird
        self.watches_frame.destroy()
        self.canvas_wf.destroy()
        self.frame_wf_out.destroy()
        self.scrollbar_wf.destroy()
        self.canvas_wf = Canvas(self.frame_wf, bg = "orange")
        self.scrollbar_wf = Scrollbar(self.frame_wf, orient = "vertical", command = self.canvas_wf.yview)
        self.frame_wf_out = Frame(self.canvas_wf, bg = self.bcolor)
        self.watches_frame = Frame(self.frame_wf_out, bg = self.bcolor)
        self.watches_frame.grid(row = 0, column = 0)

        self.watches = self.wf.search_watches(self.category_option_vars)
        self.watches_row = 1
        self.watches_column = 0
        down = FALSE
        for element in self.watches:
            watch = self.watches[element]
            watch.show_data(self.watches_frame, self.watches_row, self.watches_column)
            if down == FALSE:
                down = TRUE
                self.watches_column = self.watches_column + 1

            else:
                down = FALSE
                self.watches_column = 0
                self.watches_row = self.watches_row + 1


        self.back_button = Button(self.watches_frame, text = "Back to Start", command = lambda: self.window.show_start_page())
        self.back_button.grid(row = self.watches_row+1, column = 0)
        
        self.watches_frame.update()
        self.Watches_frame_height = self.watches_frame.winfo_height()

        self.frame_wf_out.config(height = (self.Watches_frame_height + 100))
        #part has to be after the configuration (height) of the frame, otherwise it doesn't work
        self.canvas_wf.configure(yscrollcommand = self.scrollbar_wf.set)
        self.scrollbar_wf.pack(side = RIGHT, fill = Y)
        self.canvas_wf.pack(side = "left")
        self.canvas_wf.create_window((0,0), window = self.frame_wf_out, anchor = "nw")
        self.frame_wf_out.bind("<Configure>", self.canvas_wf.configure(scrollregion = self.canvas_wf.bbox("all"), width = (self.watches_frame_width-20), height = self.window.root_height ))
