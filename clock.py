from tkinter import *
import time
import math

ft = ("Comic Sans Ms", 14)
start_x = 300
start_y = 300

length_seconds = 250
length_minutes = 250
length_hours = 200

class Clock:
    def __init__(self, master, bcolor):
        self.master = master.clock_frame
        
        """self.time_lb = Label(self.master, justify = CENTER, width = 8, font = ft)
        self.time_lb.pack(padx = 5, pady = 5)"""
        
        self.cv = Canvas(self.master, width = 600, height = 600, background = bcolor, highlightthickness = 0)
        self.cv.pack()
        self.circle = self.cv.create_oval(25,25,575,575)
        lt = time.localtime()
        
        #zeiger zeichnen
        pos_h = self.calculate_position(lt[3], "hour", length_hours)
        self.hours = self.cv.create_line(pos_h[0],pos_h[1], pos_h[2], pos_h[3], fill = "blue", width = 2)
        pos_m = self.calculate_position(lt[4], "minute", length_minutes)
        self.minutes = self.cv.create_line(pos_m[0],pos_m[1], pos_m[2], pos_m[3], fill = "blue", width = 2)
        pos_s = self.calculate_position(lt[5], "second", length_seconds)
        self.seconds = self.cv.create_line(pos_s[0],pos_s[1], pos_s[2], pos_s[3], fill = "red", width = 2)
        

        self.refresh_clock()


    def refresh_clock(self):
        lt = time.localtime()
        
        #zeiger refreshen
        pos_h = self.calculate_position(lt[3], "hour", length_hours)
        pos_m = self.calculate_position(lt[4], "minute", length_minutes)
        pos_s = self.calculate_position(lt[5], "second", length_seconds)
        self.cv.coords(self.hours, pos_h[0],pos_h[1], pos_h[2], pos_h[3])
        self.cv.coords(self.minutes, pos_m[0],pos_m[1], pos_m[2], pos_m[3])
        self.cv.coords(self.seconds, pos_s[0],pos_s[1], pos_s[2], pos_s[3])
        
        #self.time_lb.config(text = "{:02d}:{:02d}:{:02d}".format(lt[3], lt[4], lt[5]))
        self.master.after(1000, self.refresh_clock)
        
    def calculate_position(self, time, time_part, stick_length):
        # default 12 Uhr bei [start_x, start_y, start_x, start_y - sticklenght
        
        min_step_degree = 6
        degrees_hours = {3 : 0, 2 : 30, 1 : 60, 0 : 90, 11 : 120, 10 : 150, 9 : 180, 8 : 210, 7 : 240, 6 : 270, 5 : 300, 4 : 330}

        if time_part == "hour":
            if time >= 12:
                time = time - 12
            degree = degrees_hours[time]
        
        else:
            #berechnung des winkels für sekunden und Minuten
            #bei 12 uhr position sind es 90 grad, bei 3 Uhr position sind es 0 grad
            # -> bei 15 minuten (3 uhr position): ((60 -15)+15)*6 = 60*6 = 360 bzw. 0
            degree = ((60 - time) + 15)*6
        step_radian = math.radians(degree)
        stick_x = (math.cos(step_radian)*stick_length) + start_x
        stick_y = start_y - (math.sin(step_radian)*stick_length)
        return [start_x, start_y, stick_x, stick_y]