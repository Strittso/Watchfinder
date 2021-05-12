from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x400")

path= filedialog.askopenfilename() 
file = Image.open(path)
watch_image = ImageTk.PhotoImage(file)
label_image = Label(root, image = watch_image)
label_image.image = watch_image
label_image.pack()
file.save("./testfolder/IWtest.jpg")

root.mainloop()