from watch import *

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
                watchdata[fielddata[0]] = fielddata[1]
                
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
                if element not in self.categories:
                    self.categories.append(element)
                     
            watches_index = watches_index + 1
        
        return self.categories

    def get_options(self, category):
        """Method returns all options in a list of the given category."""
        options = []
        watches_index = 0
        for element in self.watches:
            watch = self.watches[watches_index]
            watch_data = watch.get_data()
    
            category_options_string = watch_data[category]
            category_options_array = category_options_string.split(",") 
            for option in category_options_array:
                if option not in options:
                    options.append(option)
                     
            watches_index = watches_index + 1
        
        return options




