#!/usr/bin/python
from tkinter import *

GUI = Tk()
GUI.title('Inventar Planner')
GUI.geometry('1280x720')
GUI.wm_attributes("-transparentcolor", "white")
GUI.resizable(0, 0)

def bye(event):
    import sys; sys.exit()


background_img = PhotoImage(file="resources\\background.gif")
products_img = PhotoImage(file="resources\\products.gif")
settings_img = PhotoImage(file="resources\\settings.gif")
help_img = PhotoImage(file="resources\\help.gif")


home_label = Canvas(GUI, width=1280, height=720)
home_label.pack()

home_label.create_image(640, 360, image=background_img)
home_label.create_text(640, 50, fill='blue', font="Times 40 bold", text='INVENTAR PLANNER')

home_label.create_image(300, 360, image=products_img, tag='prod')
home_label.create_text(300, 520, font="Times 28 bold", text='Products', tag='prod')
home_label.tag_bind('prod','<Button-1>', bye)

home_label.create_image(640, 360, image=settings_img, tag='set')
home_label.create_text(640, 520, font="Times 28 bold", text='Settings', tag='set')
home_label.bind('set', '<Button-1>', bye)

home_label.create_image(980, 360, image=help_img, tag='help')
home_label.create_text(980, 520, font="Times 28 bold", text='Help', tag='help')
home_label.tag_bind('help', '<Button-1>', bye)

GUI.mainloop()
