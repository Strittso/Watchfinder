from tkinter import *
from PIL import Image, ImageTk

class Watch:
    """Attributes of Watch are all categaories taken in the database. For initialization you already need the data from the database.
    The class has the following Methods:
    -> get_data() to return all data of the watch as a dictionary; the category is the key, the option(s) is (/are) the values"""
    def __init__(self, watchdata):
        self.watchdata = watchdata

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
            label_category.grid(row = index, column = 0, sticky = W)
            if len(self.watchdata[element]) > 1:
                value = ""
                value_index = 0
                for option in self.watchdata[element]:
                    if value_index == 0:
                        value = value + self.watchdata[element][value_index]
                    else:
                        value = value + ", " + self.watchdata[element][value_index] 
                    value_index = value_index + 1
            else:
                value = self.watchdata[element][0]
            
            label_values = Label(self.watch_frame, text = value)
            label_values.grid(row = index, column = 1, sticky = W)
            index = index + 1
        self.show_image(index)
        
        self.watch_frame.pack()
        self.frame.grid(row = row_index, column = column_index, padx = 5, pady = 5)

    def show_image(self, index):
        # shows image of the watch
        image_width = 200
        filename = "./Ressources/images/" + self.watchdata["Reference Number"][0] + ".jpg"
        file = Image.open(filename)
        file_width = file.getbbox()[2]
        reduce_factor = int(file_width / image_width)
        watch_image = ImageTk.PhotoImage(file.reduce(reduce_factor))
        label_image = Label(self.watch_frame, image = watch_image)
        label_image.image = watch_image
        label_image.grid(row = 0, rowspan = index, column = 2, sticky = W)

    def check_combination(self, combination):
        included = FALSE
        included_num = 0
        for element in combination:
            for category in self.watchdata:
                if element in self.watchdata[category]:
                    included_num = included_num + 1
        if included_num == len(combination):
            included = TRUE

        return included
    
            


