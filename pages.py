from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from dataProcessing import *
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
        self.add_data_button = Button(self.text_frame, text = "Add new Watches", command = lambda: window.show_add_data_page())
        self.add_data_button.grid(row = 2, column = 0, pady = 5)
        self.finder_button = Button(self.text_frame, text = "Start Watchfinder",command = lambda: window.show_finder_page())
        self.finder_button.grid(row = 1, column = 0, pady = 5)
        self.text_frame.pack(expand = YES, side = LEFT)

        self.clock_frame = Frame(self.start_page, background = bcolor)
        self.clock = AnalogClock(self, bcolor)
        self.clock_frame.pack(expand = YES, side = LEFT)

        self.start_page.pack(expand = YES)

    def hide(self):
        self.start_page.pack_forget()

    def show(self):
        self.start_page.pack(expand = YES)

####################################################################################################################################
class AddDataPage:
    """Class AddDataPage creates the Add Data Page, where you can add new watches to the database."""

    def __init__(self, window, bcolor):
        self.bcolor = bcolor
        self.add_data_page = Frame(window.root)
        self.add_data_page.config(background = bcolor)
        self.wf = DataProcessing()

        self.generate_add_frame()
       
        self.back_button = Button(self.add_data_page, text = "Back to Start", command = lambda: window.show_start_page())
        self.back_button.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)

        self.add_data_page.pack_forget()

    def show(self):
        self.add_data_page.pack(expand = YES)
    
    def hide(self):
        self.add_data_page.pack_forget()

    def open_watch_image(self):
        image_width = 300
        filepath = filedialog.askopenfilename()
        self.image_file = Image.open(filepath)
        file_width = self.image_file.getbbox()[2]
        reduce_factor = int(file_width / image_width)
        watch_image = ImageTk.PhotoImage(self.image_file.reduce(reduce_factor))
        self.label_image = Label(self.canvas, image = watch_image)
        self.label_image.image = watch_image
        self.label_image.pack()
    
    def delete_watch_image(self):
        try:
            self.label_image.pack_forget()
        except:
            print("no image selected")

    """def add_option(self, frame):
        
        label = Label(entry_window, text = "Please enter the categories you want to add. \nIf you want to add more than one category, \nplease seperate them by a comma.")
        label.pack()

        entry_var = StringVar()
        entry = Entry(frame, textvariable= entry_var)
        entry.pack(anchor = E)"""


    def generate_add_frame(self):
        self.add_frame = Frame(self.add_data_page)

        #entry frames for: name, reference number, Diameter, water resistance, power reserve, price
        #combobox for: dial color, case material, mechanism, glass, glass back, buckle, strap material with entry for more, except for glass back
        #checkboxes for: complication (and additional categories)

        #left side - photo and more information 
        self.left_frame = Frame(self.add_frame)
        self.canvas = Canvas(self.left_frame, width = 300, height = 300, background=self.bcolor)
        self.canvas.grid(row = 0, column = 0, pady = 5, padx = 5)
        self.image_button = Button(self.left_frame, text = "Select Picture", command = lambda: self.open_watch_image())
        self.image_button.grid(row = 1)
        self.left_frame.pack(side = LEFT)

        #returns dictionary with category as key and a string for the add type which is needed for the decision if entry, combobox or checkboxes
        self.categories = self.wf.get_categories_addtype()

        #middle - entry widgets and comboboxes, right side - checkboxes
        self.middle_frame = Frame(self.add_frame, bg = self.bcolor)
     
        middle_row_index = 0
        self.right_frame = Frame(self.add_frame, bg = self.bcolor)
        self.data = {}
        self.data_widgets = {}
        entrys_strings = []
        entrys_numbers = []
        comboboxes = []
        checkbuttons = []

        # value options: string, number, 1, more, yes_no
        for category in self.categories.keys():
           
           #einzelne frames und widgets in dict o.Ä. speichern?????????????????????????????????????????
            if self.categories[category] == "string":
                label = Label(self.middle_frame, text = category, bg = self.bcolor)
                label.grid(row = middle_row_index, column = 0, padx = 5, pady = 5, sticky=W)
                entry_string_var = StringVar()
                entry = Entry(self.middle_frame, textvariable = entry_string_var)
                entry.grid(row = middle_row_index, column = 1, padx = 5, pady = 5, sticky=W)
                entrys_strings.append(entry)
                middle_row_index = middle_row_index + 1
                self.data[category] = entry_string_var
                
                
            if self.categories[category] == "number":
                label = Label(self.middle_frame, text = category, bg = self.bcolor)
                label.grid(row = middle_row_index, column = 0, padx = 5, pady = 5, sticky=W)
                entry_number_var = DoubleVar()
                entry = Entry(self.middle_frame, textvariable = entry_number_var, width=8)
                entry.grid(row = middle_row_index, column = 1, padx = 5, pady = 5, sticky=W)
                entrys_numbers.append(entry)
                middle_row_index = middle_row_index + 1
                self.data[category] = entry_number_var

            if self.categories[category] == "1":
                label = Label(self.middle_frame, text = category, bg = self.bcolor)
                label.grid(row = middle_row_index, column = 0, padx = 5, pady = 5, sticky=W)
                options = self.wf.get_options(category)
                selected = StringVar()
                combobox = ttk.Combobox(self.middle_frame, values = options, textvariable = selected)
                combobox.grid(row = middle_row_index, column = 1, sticky=W, padx = 5, pady = 5)
                comboboxes.append(combobox)
                middle_row_index = middle_row_index + 1
                self.data[category] = selected

            if self.categories[category] == "yes_no":
                option_vars = {}
                option_vars["Yes"] = IntVar()
                option_vars["No"] = IntVar()
                yes_no_frame = Frame(self.right_frame, bg = self.bcolor)
                label = Label(yes_no_frame, text = category, bg = self.bcolor)
                label.pack(anchor=W)
                yes_checkbutton = Checkbutton(yes_no_frame, text = "Yes", variable=option_vars["Yes"], bg = self.bcolor)
                yes_checkbutton.pack(anchor=W)
                no_checkbutton = Checkbutton(yes_no_frame, text = "No", variable=option_vars["No"],bg = self.bcolor)
                no_checkbutton.pack(anchor=W)
                checkbuttons.append(yes_checkbutton)
                checkbuttons.append(no_checkbutton)
                yes_no_frame.pack(anchor=W)
                self.data[category] = option_vars


            if self.categories[category] == "more":
                option_vars = {}
                checkbuttons_frame = Frame(self.right_frame, bg = self.bcolor)
                label = Label(checkbuttons_frame, text = category, bg = self.bcolor)
                label.pack(anchor=W)
                options = self.wf.get_options(category)
                
                for option in options:
                    option_vars[option] = IntVar()
                    checkbutton = Checkbutton(checkbuttons_frame, text = option, variable = option_vars[option], bg = self.bcolor)
                    checkbutton.pack(anchor=W)
                    checkbuttons.append(checkbutton)

                """button = Button(checkbuttons_frame, text = "Add new Option", command = lambda: self.add_option(checkbuttons_frame))
                button.pack(side = BOTTOM, anchor = E)"""

                self.data[category] = option_vars

                checkbuttons_frame.pack(anchor=W)
        
        
        self.data_widgets["String"] = entrys_strings
        self.data_widgets["Number"] = entrys_numbers
        self.data_widgets["Combobox"] = comboboxes
        self.data_widgets["Checkbutton"] = checkbuttons    
            
        self.middle_frame.pack(side = LEFT)
        self.right_frame.pack(side = RIGHT)

        self.image_file = 0
        self.save_button = Button(self.add_data_page, text = "Save", command = lambda: [self.wf.save_watches_data(self.image_file, self.data, self.data_widgets), self.delete_watch_image()])
        self.save_button.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = W)
        

        self.add_frame.grid(row = 0, column = 0, padx = 5, pady = 5)




###################################################################################################################################
class FinderPage:

    def __init__(self, window, bcolor):
        self.window = window
        self.bcolor = bcolor
        self.wf = DataProcessing()

        self.finder_page = Frame(self.window.root, bg = self.bcolor)        

        self.watches_frame_width = (0.78*self.window.root_width)
        self.frame_wf = Frame(self.finder_page, bg = bcolor)
        self.canvas_wf = Canvas(self.frame_wf, bg = "orange")
        self.frame_wf_out = Frame(self.canvas_wf, bg = self.bcolor)
        self.watches_frame = Frame(self.finder_page, bg = self.bcolor)
        self.scrollbar_wf = Scrollbar(self.frame_wf, orient = "vertical", command = self.canvas_wf.yview)
        
        self.finder_page.pack_forget()

    def show(self):
        self.finder_page.pack(expand = YES, fill = BOTH)
        self.watches = self.wf.get_watches()
        self.generate_categories_frame()
        self.refresh_page()
        self.frame_wf.place(x = self.cf_width, y = 0, width = self.watches_frame_width, height = self.window.root_height)


    def hide(self):
        self.finder_page.pack_forget()

    def generate_categories_frame(self):
        self.cf_width = (0.22*self.window.root_width)
        self.frame_cf = Frame(self.finder_page, bg = self.bcolor)
        self.frame_cf.place(x = 0, y = 0, width = self.cf_width, height = self.window.root_height)
        self.canvas_cf = Canvas(self.frame_cf, bg = "orange")

        self.frame_cf_out = Frame(self.canvas_cf, bg = self.bcolor)
        self.categories_frame = Frame(self.frame_cf_out, bg = self.bcolor)
        self.categories_frame.grid(row = 0, column = 0)
        self.categories = self.wf.get_categories()

        self.label = Label(self.categories_frame, text = "Please select Categoies", bg = self.bcolor, font = "30")
        self.label.grid(row = 0, column = 0, pady = 20, padx = 20, sticky = W)

        row_index = 1
        self.category_frames = {}
        self.option_frames = {}
        self.options_checkbuttons = {}
        self.category_option_vars = {}
        self.categories_type = self.wf.get_categories_addtype()
        for category in self.categories:
            self.category_frames[category] = Frame(self.categories_frame, bg = self.bcolor)
            category_lb = Label(self.category_frames[category], text = category, bg = self.bcolor)
            category_lb.grid(row = 0, column = 0, sticky = W)


            self.option_frames[category] = Frame(self.category_frames[category], bg = self.bcolor)
            options = self.wf.get_options(category)

            

            if self.categories_type[category] == "number":
                print(category)
                
                label_min = Label(self.option_frames[category], text = "From:", bg = self.bcolor)
                label_min.grid(row = 0, column = 0, padx = 5, pady = 5, sticky=W)
                label_max = Label(self.option_frames[category], text = "To:", bg = self.bcolor)
                label_max.grid(row = 1, column = 0, padx = 5, pady = 5, sticky=W)
                entry_min = DoubleVar()
                entry_max = DoubleVar()
                entry_min = Entry(self.option_frames[category], textvariable = entry_min, width=8)
                entry_min.grid(row = 0, column = 1, padx = 5, pady = 5, sticky=W)
                entry_max = Entry(self.option_frames[category], textvariable = entry_max, width=8)
                entry_max.grid(row = 1, column = 1, padx = 5, pady = 5, sticky=W)
                option_vars = {"min":entry_min, "max":entry_max}
                
            else:
                option_vars = {}
                option_index = 0
                for option in options:
                    option_vars[option] = IntVar()
                    self.options_checkbuttons[option] = Checkbutton(self.option_frames[category], text = option, variable = option_vars[option], bg = self.bcolor)
                    self.options_checkbuttons[option].grid(row = option_index, column = 0, sticky = W)
                    option_index = option_index + 1

            self.category_option_vars[category] = option_vars 
            self.option_frames[category].grid(row = 1, column = 0, sticky = W)
            
            self.category_frames[category].grid(row = row_index, column = 0, padx = 20, pady = 5, sticky = W)
            row_index = row_index + 1

        self.search_button = Button(self.categories_frame, text = "Search", command = lambda: self.refresh_page())
        self.search_button.grid(row = row_index, column = 0, pady = 5)
      
        # to get the height of a frame just works when every widget is placed and only after Frame.update()
        self.scrollbar_cf = Scrollbar(self.frame_cf, orient = "vertical", command = self.canvas_cf.yview)

        self.categories_frame.update()
        self.cf_height = self.categories_frame.winfo_height()
        self.frame_cf_out.config(height = (self.cf_height))
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
        self.watches_frame_height = self.watches_frame.winfo_height()

        self.frame_wf_out.config(height = (self.watches_frame_height))
        #part has to be after the configuration (height) of the frame, otherwise it doesn't work
        self.canvas_wf.configure(yscrollcommand = self.scrollbar_wf.set)
        self.scrollbar_wf.pack(side = RIGHT, fill = Y)
        self.canvas_wf.pack(side = "left")
        self.canvas_wf.create_window((0,0), window = self.frame_wf_out, anchor = "nw")
        self.frame_wf_out.bind("<Configure>", self.canvas_wf.configure(scrollregion = self.canvas_wf.bbox("all"), width = (self.watches_frame_width-20), height = self.window.root_height ))

