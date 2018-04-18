#!/usr/bin/python
from tkinter import *

# WARNING!
#
# treba este dodat zopar veci, zatial tolko funkcionalit som zvladol pridat..
# treba aspon tie produkty poriesit..nemusi byt uplne funkcny program..
# + ten padding nejak zrusit, neviem preco to ukazuje
# + pristupy

# hej, viem ze to vyzera napicu zatial, aj backgound je napicu jasne, viem.. ale treba tu funkcionalitu upravit dorobit..

class InventarPlanner(Tk):

    def __init__(self):
        Tk.__init__(self)

        self.title('Inventar Planner')
        self.geometry('1280x720')
        self.resizable(0, 0)
        self._frame = None
        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class HomePage(Frame):

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
        home_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='INVENTAR PLANNER')

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
        #               tuna este treba pridat nejake dialogove okno na prihlasenie sa
        #home_label.tag_bind('signup', '<ButtonPress-1>', lambda event: controller.switch_frame(HelpPage))


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

    def __init__(self, controller):
        Frame.__init__(self, controller)

        self.controller = controller

        settings_label = Canvas(self, width=1280, height=720)
        settings_label.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img

        settings_label.create_image(640, 360, image=background_img)
        settings_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='Settings')

        back_img = PhotoImage(file="resources/back.gif")
        self.back = back_img

        settings_label.create_image(100, 60, image=back_img, tag='back')
        settings_label.tag_bind('back', '<Button-1>', lambda event: controller.switch_frame(HomePage))

        settings_label.create_text(300, 300, font="Times 20 bold", text='Set up reminder')
        settings_label.create_text(300, 350, font="Times 20 bold", text='Remind upcoming ending of a product')
        settings_label.create_text(300, 400, font="Times 20 bold", text='Limit at the given month: ')

        save_btn = Button(text ="Save", font="Times 20 bold", command=lambda: controller.switch_frame(HomePage))
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
    app = InventarPlanner()
    app.mainloop()
