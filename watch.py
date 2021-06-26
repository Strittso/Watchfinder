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

        label_watch = ""
        index = 1
        for element in self.watchdata:
            label_watch = label_watch + element + ": "

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
            label_watch = label_watch + value + "\n"
            index = index + 1
        
        self.watch_image = self.get_image()
        self.button = Button(master, text=label_watch, image=self.watch_image, width = 470, height = 300, compound="right", command = lambda:self.show_details())
        self.button.image = self.watch_image
        self.button.grid(row = row_index, column = column_index, padx = 5, pady = 5)

    def show_details(self):
        self.window = Toplevel()
       
        image_width = 300
        try:
            filename = "./Ressources/images/" + self.watchdata["Reference Number"][0] + ".jpg"
            file = Image.open(filename)
        except FileNotFoundError:
            filename = "./Ressources/images/" + self.watchdata["Reference Number"][0] + ".png"
            file = Image.open(filename)

        file = Image.open(filename)
        file_width = file.getbbox()[2]

        factor = file_width / image_width

        reduce_factor = round(factor)
        watch_image = ImageTk.PhotoImage(file.reduce(reduce_factor))

        label_image = Label(self.window, image = watch_image)
        label_image.image = watch_image
        label_image.grid(row = 0, column = 0, columnspan=2)
        index = 1
        for element in self.watchdata:
            label_category = Label(self.window, text = element)
            label_category.grid(row = index, column = 0)

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
           
            label_category = Label(self.window, text = value)
            label_category.grid(row = index, column = 1)
            index = index + 1

        self.window.mainloop()


    def get_image(self):
        # returns image of the watch
        image_width = 200
        try:
            filename = "./Ressources/images/" + self.watchdata["Reference Number"][0] + ".jpg"
            file = Image.open(filename)
        except FileNotFoundError:
            filename = "./Ressources/images/" + self.watchdata["Reference Number"][0] + ".png"
            file = Image.open(filename)
        file = Image.open(filename)
        file_width = file.getbbox()[2]
        
        factor = file_width / image_width
        
        reduce_factor = round(factor)
        watch_image = ImageTk.PhotoImage(file.reduce(reduce_factor))
        
        return watch_image

    def check_combination(self, combination, numbers):
        included = FALSE
        included_num = 0
        for element in combination:
            for category in self.watchdata:
                if element in self.watchdata[category]:
                    included_num = included_num + 1
        numbers_included = 0
        for category in numbers:
            if numbers[category]["min"] != '':
                min = float(numbers[category]["min"])
            else:
                min = 0

            if numbers[category]["max"] != '':
                max = float(numbers[category]["max"])
            else:
                max = 0

            if (min == 0) & (max == 0):
                numbers_included = numbers_included + 1
            if (float(self.watchdata[category][0]) >= min) & (float(self.watchdata[category][0]) <= max):
                numbers_included = numbers_included + 1
    
        if (included_num == len(combination)) & (numbers_included == len(numbers)):
            included = TRUE
            

        return included


        
        
        

    
            


