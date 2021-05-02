from watch import *

def read_watches_data(filename):
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

watches_data = read_watches_data("./ressources/watches.csv")
watches = {}
element_index = 0
for element in watches_data:
    watches[element_index] = Watch(watches_data[element_index])
    element_index = element_index+1

print(watches)


