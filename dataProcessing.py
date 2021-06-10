
from watch import *
import itertools as it
from tkinter import messagebox as mb


class DataProcessing:

    """Watchfinder class with all important functions for finding watches and to help design the finder page:
    -> read_wathes_data(filename) reads the data from filename and returns the data as a dictionary; key are numbers starting from 0, value ist the data for one watch as a dictionary
    -> get_watches() returns a dictionary similar to the one in read_watches_data(filename) but now the value are objects of the class Watch
    -> get_categories() searches for different categories in all watches and returns all found categories in a list
    -> get_options() returns all options in a list of the given category """

    # --> static Methods?

    def __init__(self):
        self.watches = self.get_watches()

    def read_watches_data(self, filename):
        f = open(filename, "r", encoding="UTF-8")
        watches_data = f.readlines()
        f.close()

        watchdata_list = {}
        line_index = 0
        for line in watches_data:
            fieldswatchdata = line.strip("\n").split(";")
            watchdata = {}
            for field in fieldswatchdata:
                fielddata = field.split(":")        
                fd_separated = fielddata[1].split(",")
                watchdata[fielddata[0]] = fd_separated
                
            watchdata_list[line_index]  = watchdata
            line_index = line_index+1
        return watchdata_list

    def get_watches(self):
        watches_data = self.read_watches_data("./ressources/watches.csv")
        watches = {}
        element_index = 0
        for element in watches_data:
            watches[element_index] = Watch(watches_data[element_index])
            element_index = element_index+1
        
        return watches

    def save_watches_data(self, image_file, entered_watchdata, data_widgets):
        f = open("./Ressources/watches.csv", "a")
        data = entered_watchdata
        new_watch_data_str = ""
        categories = self.get_categories_addtype()
        for category in categories:
            is_dictionary = isinstance(data[category], dict)

            if is_dictionary:
                selected = ""
                for element in data[category]:

                    if data[category][element].get() == 1:
                        selected = selected + element + ","
                
                new_watch_data_str = new_watch_data_str + category + ":" + selected.strip(",") + ";"
                
            else:
                value = data[category].get()
                new_watch_data_str = new_watch_data_str + category + ":" + str(value) + ";"
            
        try:
            image_filepath = "./Ressources/images/" + data["Reference Number"].get() + ".jpg"
            try:
                image_file.save(image_filepath)
            except OSError:
                image_filepath = "./Ressources/images/" + data["Reference Number"].get() + ".png"
            new_watch_data_str = new_watch_data_str.strip(";")
            f.write("\n" + new_watch_data_str) 
        except AttributeError:
            mb.showerror("No Picture","Please select a picture to save the new watch!")
        

        else:
            mb.showinfo("Saved","Saved new watch successfully!")

        

        f.close()


        #clear the checkbuttons, entries and comboboxes and also the image field to save the next watch
        widgets = data_widgets
        del image_file

        for element in widgets["String"]:
            element.delete(0, "end")

        for element in widgets["Number"]:
            element.delete(0, "end")
            element.insert(0, 0.0)
        
        for element in widgets["Combobox"]:
            element.set("")

        for element in widgets["Checkbutton"]:
            element.deselect()
    
    def get_categories_addtype(self):
        f = open("./Ressources/categories.csv", "r", encoding="UTF-8")
        categiries_data = f.readlines()
        f.close()

        categories_list = {}
        for line in categiries_data:
            fields = line.strip("\n").strip(" ").split(":")
            categories_list[fields[0]] = fields[1]

        return(categories_list)


    def get_categories(self):
        """Method searches for different categories in all watches and returns all found categories in a list"""
        self.watches = self.get_watches()
        self.categories = []
        watches_index = 0
        for element in self.watches:
            watch = self.watches[watches_index]
            watch_data = watch.get_data()
            for element in watch_data:
                if element != "Reference Number" and element != "Name":
                    if element not in self.categories:
                        self.categories.append(element)
                     
            watches_index = watches_index + 1
        
        return self.categories

    def get_options(self, category):
        """Method returns all options in a list of the given category except for Reference Number and Name."""
        self.watches = self.get_watches()
        options = []
        watches_index = 0
        for element in self.watches:
            watch = self.watches[watches_index]
            watch_data = watch.get_data()
            category_options_array = watch_data[category] 
            for option in category_options_array:
                if option not in options:
                    options.append(option)
                     
            watches_index = watches_index + 1
        
        return options

    #komplikation geht noch nicht wenn die Uhr mehr als 1 Komplikation hat
    def search_watches(self, category_option_vars):
        self.watches = self.get_watches()

        selected_options = {}
        for category in category_option_vars:
            option_vars = category_option_vars[category]
            selected = []
            for element in option_vars:
                if option_vars[element].get() == 1:
                    selected.append(element)
            if selected:
                selected_options[category] = selected

        filtered_watches = {}
        if selected_options.values(): 
            
            # mit Modul itertool alle Möglichen Kombinationen in eine Liste eintragen lassen
            # z.B. gewäglt sind:{"Brand": ["IWC","Tissot"], "Size":[40, 42]}
            # -> Komnbinationen = [(IWC,40),(IWC,42),(Rolex,40),(Rolex,42)] 
            options_list = []
            for category in selected_options:
                options_list.append(selected_options[category])

            combinations = list(it.product(*options_list))
            index = 0
            for combination in combinations:
                for watch in self.watches:
                    included = self.watches[watch].check_combination(combination)
                    if included == TRUE and self.watches[watch] not in filtered_watches.values():
                        filtered_watches[index] = self.watches[watch] 
                        index = index + 1
        else:
            filtered_watches = self.watches
        
        return filtered_watches
                        