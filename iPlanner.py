#!/usr/bin/python
from tkinter import *

GUI = Tk()
GUI.title('Inventar Planner')
GUI.geometry('1280x720')
#GUI.wm_attributes('-transparentcolor', GUI['bg'])
GUI.resizable(0, 0)

def bye(event):
    import sys; sys.exit()


background_img = PhotoImage(file="resources\\background.gif")
products_img = PhotoImage(file="resources\\products.gif")
settings_img = PhotoImage(file="resources\\settings.gif")
help_img = PhotoImage(file="resources\\help.gif")


bg_label = Canvas(GUI, width=1280, height=720)
bg_label.create_image(640, 360, image=background_img)
bg_label.create_text(640, 50, fill='blue', font="Times 40 bold", text='INVENTAR PLANNER')
bg_label.pack()


products = Label(bg_label, image=products_img)
products.place(x=180, y=225)
products.bind('<Button-1>', bye)
products_label = Label(bg_label, text='Products', font=("Courier",  28))
products_label.place(x=215, y=500)
#products_label.config(bg='systemTransparent')
products_label.bind('<Button-1>', bye)

settings = Label(bg_label, image=settings_img)
settings.place(x=505, y=225)
settings.bind('<Button-1>', bye)
settings_label = Label(bg_label, text='Settings', font=("Courier",  28))
settings_label.place(x=550, y=500)
settings_label.bind('<Button-1>', bye)

help = Label(bg_label, image=help_img)
help.place(x=850, y=225)
help.bind('<Button-1>', bye)
help_label = Label(bg_label, text='Help', font=("Courier",  28))
help_label.place(x=940, y=500)
help_label.bind('<Button-1>', bye)

GUI.mainloop()