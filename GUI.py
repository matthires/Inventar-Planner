#!/usr/bin/python
from tkinter import *
from tkinter.font import Font


class InventoryPlanner(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title('Inventory Planner')
        self.geometry('1280x720')
        self.resizable(0, 0)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class HomePage(Frame):

    def sign_up(self):
        root = Toplevel(width=400, height=220)
        sign_up_label = Label(root, width=100, height=60)
        sign_up_label.place(x=10, y=10)
        Label(sign_up_label, text="Enter your username and password!", font="Times 12 bold").place(x=100, y=10)
        Label(sign_up_label, text="User Name").place(x=50, y=50)
        user_name = Entry(sign_up_label, bd=5)
        user_name.place(x=150, y=50)
        Label(sign_up_label, text="Password").place(x=50, y=100)
        password = Entry(sign_up_label, bd=5)
        password.place(x=150, y=100)
        sign_up_button = Button(sign_up_label, text='Sign Up', command=root.destroy)
        sign_up_button.place(x=180, y=150)
        sign_up_label.mainloop()

    def __init__(self, controller):
        Frame.__init__(self, controller)

        self.controller = controller

        home_label = Canvas(self, width=1280, height=720)
        home_label.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img
        products_img = PhotoImage(file="resources/products.gif")
        self.products = products_img
        settings_img = PhotoImage(file="resources/settings.gif")
        self.settings = settings_img
        help_img = PhotoImage(file="resources/help.gif")
        self.help = help_img
        user_img = PhotoImage(file="resources/user.gif")
        self.user = user_img

        home_label.create_image(640, 360, image=background_img)
        home_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='INVENTORY PLANNER')

        home_label.create_image(300, 360, image=products_img, tag='prod')
        home_label.create_text(300, 520, font="Times 28 bold", text='Products', tag='prod')
        home_label.tag_bind('prod', '<ButtonPress-1>', lambda event: controller.switch_frame(ProductsPage))

        home_label.create_image(640, 360, image=settings_img, tag='set')
        home_label.create_text(640, 520, font="Times 28 bold", text='Settings', tag='set')
        home_label.tag_bind('set', '<ButtonPress-1>', lambda event: controller.switch_frame(SettingsPage))

        home_label.create_image(980, 360, image=help_img, tag='help')
        home_label.create_text(980, 520, font="Times 28 bold", text='Help', tag='help')
        home_label.tag_bind('help', '<ButtonPress-1>', lambda event: controller.switch_frame(HelpPage))

        home_label.create_image(1180, 60, image=user_img, tag='signup')
        home_label.create_text(1180, 100, font="Times 12 bold", text='Sign up', tag='signup')

        home_label.tag_bind('signup', '<ButtonPress-1>', lambda event: self.sign_up())


class ProductsPage(Frame):

    def __init__(self, controller):
        Frame.__init__(self, controller)

        self.controller = controller

        products_label = Canvas(self, width=1280, height=720)
        products_label.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img

        products_label.create_image(640, 360, image=background_img)
        products_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='Products')

        back_img = PhotoImage(file="resources/back.gif")
        self.back = back_img

        products_label.create_image(100, 60, image=back_img, tag='back')

        products_label.tag_bind('back', '<Button-1>', lambda event: controller.switch_frame(HomePage))


class SettingsPage(Frame):

    #def set_reminder(self):
     #   if not self.is_reminder_set:
     #       self.text_color.set("grey")
     #       self.max_months.set(0)
      #  else:
       #     self.text_color.set("grey")
        #    self.max_months.set(12)

    def __init__(self, controller):
        Frame.__init__(self, controller)

        self.controller = controller
        self.is_reminder_set = False

        self.background_img = PhotoImage(file="resources/background.gif")
        self.back_img = PhotoImage(file="resources/back.gif")

        settings_canvas = Canvas(self, width=1280, height=720)
        settings_canvas.pack(side='top', fill='x')
        self.settings_label = Label(self, width=130, height=30)
        self.settings_label.place(x=190, y=110)

        settings_canvas.create_image(640, 360, image=self.background_img)
        settings_canvas.create_text(640, 60, fill='blue', font="Times 40 bold", text='Settings')

        settings_canvas.create_image(100, 60, image=self.back_img, tag='back')
        settings_canvas.tag_bind('back', '<Button-1>', lambda event: controller.switch_frame(HomePage))

        Label(self.settings_label, font="Times 20 bold", text='Set up reminder').place(x=200, y=50)
        #self.reminder = Checkbutton(self.settings_label, width=4, variable=self.is_reminder_set,
        #                            onvalue=True, offvalue=False, command=self.set_reminder())
        #self.reminder.place(x=400, y=59)

        self.text_color = "black"
        self.max_months = 12
        self.reminder_label = Label(self.settings_label, foreground=self.text_color, font="Times 20 bold",
                                    text='Remind upcoming ending of a product          months before')
        self.months = Spinbox(self.settings_label, from_=0, to=self.max_months, width=3, font='Helvetica 14 bold')

        self.reminder_label.place(x=120, y=110)

        self.months.place(x=580, y=118)

        Label(self.settings_label, font="Times 20 bold", text='Limit at the given month: ').place(x=200, y=170)
        self.entry = Entry(self.settings_label, bd=5, font='Helvetica 14 bold')
        self.entry.place(x=510, y=168, width=100)
        Label(self.settings_label, font="Times 20 bold", text='€').place(x=620, y=170)

        save_btn = Button(text="Save", font="Times 20 bold", command=lambda: controller.switch_frame(HomePage))
        save_btn.place(x=640, y=620)


class HelpPage(Frame):

    def __init__(self, controller):
        Frame.__init__(self, controller)

        self.controller = controller

        help_label = Canvas(self, width=1280, height=720)
        help_label.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img

        help_label.create_image(640, 360, image=background_img)
        help_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='Help')

        back_img = PhotoImage(file="resources/back.gif")
        self.back = back_img

        help_label.create_image(100, 60, image=back_img, tag='back')
        help_label.tag_bind('back', '<Button-1>', lambda event: controller.switch_frame(HomePage))


if __name__ == "__main__":
    app = InventoryPlanner()
    app.mainloop()
