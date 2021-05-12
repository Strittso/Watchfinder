from watch import *
import itertools as it

class Watchfinder:

    """Watchfinder class with all important functions for finding watches and to help design the finder page:
    -> read_wathes_data(filename) reads the data from filename and returns the data as a dictionary; key are numbers starting from 0, value ist the data for one watch as a dictionary
    -> get_watches() returns a dictionary similar to the one in read_watches_data(filename) but now the value are objects of the class Watch
    -> get_categories() searches for different categories in all watches and returns all found categories in a list
    -> get_options() returns all options in a list of the given category """

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

    def get_categories(self):
        """Method searches for different categories in all watches and returns all found categories in a list"""
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
                        