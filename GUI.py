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
home_label.create_text(640, 50, font="Times 28 bold", text='INVENTAR PLANNER')

home_label.create_image(300, 360, image=products_img)
products_label = Label(home_label, text='Products', font=("Courier",  28)).place(x=215, y=500)
#products_label.config(bg='systemTransparent')
#products_label.bind('<Button-1>', bye)

home_label.create_image(640, 360, image=settings_img)
settings_label = Label(home_label, text='Settings', font=("Courier",  28)).place(x=560, y=500)
#settings_label.bind('<Button-1>', bye)

home_label.create_image(980, 360, image=help_img)
help_label = Label(home_label, text='Help', font=("Courier",  28)).place(x=940, y=500)
#help_label.bind('<Button-1>', bye)

#title.bind('<Button-1>', bye)


GUI.mainloop()