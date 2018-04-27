#!/usr/bin/python
import tkinter.filedialog as tkfd
import tkinter.messagebox as tm
from tkinter import *

from Product import Product


class InventoryPlanner(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title('Inventory Planner')
        self.geometry('1280x720')
        self.resizable(0, 0)

        self.frames = {}
        for F in (HomePage, ProductsPage, SettingsPage, HelpPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(Frame):

    def sign_out(self, controller):
        self.sign_out_frame.destroy()
        tm.showinfo("Signed out.", "You were successfully signed out.")
        self.home_label.itemconfig(self.signup_txt, text="Sign up")
        controller.is_admin = False

    def sign_up(self, controller):
        if not controller.is_admin:
            self.signup_frame = Toplevel(width=400, height=220)
            self.signup_frame.title('Sign up')
            sign_up_label = Label(self.signup_frame, width=100, height=60)
            sign_up_label.place(x=10, y=10)
            Label(sign_up_label, text="Enter your username and password!", font="Times 12 bold").place(x=100, y=10)
            Label(sign_up_label, text="User Name").place(x=50, y=50)
            self.user_name = Entry(sign_up_label, bd=5)
            self.user_name.place(x=150, y=50)
            Label(sign_up_label, text="Password").place(x=50, y=100)
            self.password = Entry(sign_up_label, bd=5, show="*")
            self.password.place(x=150, y=100)
            sign_up_button = Button(sign_up_label, text='Sign Up', command=lambda: self._login_(controller))
            self.password.bind('<Return>', lambda event: self._login_(controller))
            sign_up_button.place(x=180, y=150)
            sign_up_label.mainloop()
        else:
            self.sign_out_frame = Toplevel(width=360, height=160)
            self.sign_out_frame.title('Profile')
            sign_out_label = Label(self.sign_out_frame, width=100, height=60)
            sign_out_label.place(x=10, y=10)
            txt='Signed up as ' + self.user.get() + '.'
            Label(sign_out_label, text=txt, font="Times 12 bold").place(x=100, y=20)
            Label(sign_out_label, text='Do you want to sign out?', font="Times 12 bold").place(x=90, y=60)
            yes_btn = Button(sign_out_label, text="Yes", font="Times 12 bold",
                             command=lambda: self.sign_out(controller))
            yes_btn.place(x=120, y=100)
            no_btn = Button(sign_out_label, text="No", font="Times 12 bold",
                            command=lambda: self.sign_out_frame.destroy())
            no_btn.place(x=160, y=100)

    def _login_(self, controller):
        username = self.user_name.get()
        password = self.password.get()

        if username == "admin" and password == "admin":
            tm.showinfo("Login info", "Welcome " + self.user.get())
            self.signup_frame.destroy()
            self.home_label.itemconfig(self.signup_txt, text=self.user.get())
            controller.is_admin = True
        else:
            tm.showerror("Login error!", "Incorrect username or password!")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.signup_frame = self
        self.sign_out_frame = self
        self.controller = controller
        self.user_name = StringVar()
        self.password = StringVar()
        self.user = StringVar()
        self.user.set('Admin')
        controller.is_admin = False

        self.home_label = Canvas(self, width=1280, height=720)
        home_label = self.home_label
        home_label.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img
        products_img = PhotoImage(file="resources/products.gif")
        self.products = products_img
        settings_img = PhotoImage(file="resources/settings.gif")
        self.settings = settings_img
        help_img = PhotoImage(file="resources/help.gif")
        self.help = help_img
        signup_img = PhotoImage(file="resources/user.gif")
        self.signup_img = signup_img

        home_label.create_image(640, 360, image=background_img)
        home_label.create_text(640, 60, fill='blue', font="Times 40 bold", text='INVENTORY PLANNER')

        home_label.create_image(300, 360, image=products_img, tag='prod')
        home_label.create_text(300, 520, font="Times 28 bold", text='Products', tag='prod')
        home_label.tag_bind('prod', '<ButtonPress-1>', lambda event: controller.show_frame('ProductsPage'))

        home_label.create_image(640, 360, image=settings_img, tag='set')
        home_label.create_text(640, 520, font="Times 28 bold", text='Settings', tag='set')
        home_label.tag_bind('set', '<ButtonPress-1>', lambda event: controller.show_frame('SettingsPage'))

        home_label.create_image(980, 360, image=help_img, tag='help')
        home_label.create_text(980, 520, font="Times 28 bold", text='Help', tag='help')
        home_label.tag_bind('help', '<ButtonPress-1>', lambda event: controller.show_frame('HelpPage'))

        home_label.create_image(1180, 60, image=signup_img, tag='signup')
        self.signup_txt = home_label.create_text(1180, 100, font="Times 12 bold", text='Sign up', tag='signup')

        home_label.tag_bind('signup', '<ButtonPress-1>', lambda event: self.sign_up(controller))


class ProductsPage(Frame):
    #new_prod =

    def add_product(self):
        img = self.prod_image
        name = self.prod_name_entry.get()
        date = self.prod_date_entry.get()
        num = self.num_entry.get()
        endurance = self.endurance_entry.get()
        price = self.price_entry.get()
        self.new_prod = Product(self.prod_label, img, name, date, num, endurance, price)
        self.new_prod.add_to_label(self.prod_label)
        self.products.insert(len(self.products), self.new_prod)
        self.new_prod_frame.destroy()

    def load_pic(self):
        img_path = tkfd.askopenfilename(filetypes=[("GIF", "*.gif")], title='Select a picture')
        self.prod_image = PhotoImage(file=img_path)
        self.product_img.configure(image=self.prod_image)

    def new_product(self):
        self.new_prod_frame = Toplevel(width=800, height=220)
        self.new_prod_frame.title('New product')
        new_product_label = Label(self.new_prod_frame, width=800, height=220)
        new_product_label.place(x=10, y=10)
        Label(new_product_label, text="Product name", font="Times 12 bold").place(x=150, y=40)
        Label(new_product_label, text="Buying date", font="Times 12 bold").place(x=365, y=40)
        Label(new_product_label, text="Num", font="Times 12 bold").place(x=500, y=40)
        Label(new_product_label, text="Endurance(months)", font="Times 12 bold").place(x=550, y=40)
        Label(new_product_label, text="Price(€)", font="Times 12 bold").place(x=700, y=40)

        self.product_img = Label(new_product_label, image=self.no_photo)
        self.product_img.place(x=60, y=35)
        self.product_img.bind('<ButtonPress-1>', lambda event: self.load_pic())
        change_pic = Label(new_product_label, text='Change pic', fg='blue', font='Helvetica 9')
        change_pic.place(x=60, y=90)
        change_pic.bind('<ButtonPress-1>', lambda event: self.load_pic())

        self.prod_name_entry = Entry(new_product_label, bd=5, font='Helvetica 14 bold')
        self.prod_name_entry.place(x=150, y=70, width=200)
        self.prod_date_entry = Entry(new_product_label, bd=5, font='Helvetica 14')
        self.prod_date_entry.place(x=365, y=70, width=120)
        self.num_entry = Spinbox(new_product_label, from_=1, to=120, width=3, font='Helvetica 14')
        self.num_entry.place(x=500, y=75)
        self.endurance_entry = Spinbox(new_product_label, from_=0, to=48, width=3, font='Helvetica 14')
        self.endurance_entry.place(x=580, y=75)
        self.price_entry = Entry(new_product_label, bd=5, font='Helvetica 14')
        self.price_entry.place(x=690, y=70, width=80)

        add_prod_btn = Button(new_product_label, text="Add", font="Times 12 bold",
                              command=lambda: self.add_product())
        add_prod_btn.place(x=400, y=150)

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller

        self.new_prod_frame = self
        self.no_photo = PhotoImage(file="resources/empty_img.gif")
        self.prod_image = PhotoImage(file="resources/empty_img.gif")
        self.product_img = Label()
        self.products = []

        products_canvas = Canvas(self, width=1280, height=720)
        products_canvas.pack(side="top", fill="x")

        background_img = PhotoImage(file="resources/background.gif")
        self.bg = background_img

        products_canvas.create_image(640, 360, image=background_img)
        products_canvas.create_text(640, 60, fill='blue', font="Times 40 bold", text='Products')

        back_img = PhotoImage(file="resources/back.gif")
        self.back = back_img

        products_canvas.create_image(100, 60, image=back_img, tag='back')
        products_canvas.tag_bind('back', '<Button-1>', lambda event: controller.show_frame('HomePage'))

        self.prod_label = Canvas(products_canvas, bg='grey')
        self.prod_label.place(x=150, y=100, width=980, height=500)
        self.scrollbar = Scrollbar(self.prod_label, orient=VERTICAL)
        self.scrollbar.place(x=962, y=1, height=500)
        self.scrollbar.config(command=self.prod_label.yview)
        products_txt = "Product name         Buying date   Num   Endurance(mth)  Price(€)"
        Label(self.prod_label, bg='grey', text=products_txt, font="Times 22 bold").place(x=150, y=10)

        delete_prod_btn = Button(self.prod_label, text="X", font="Times 20 bold",
                                 command=lambda: self.new_prod.delete)
        delete_prod_btn.place(x=30, y=620)
        new_prod_btn = Button(products_canvas, text="Add product +", font="Times 20 bold",
                              command=lambda: self.new_product())
        new_prod_btn.place(x=550, y=620)


class SettingsPage(Frame):

    def set_reminder(self):
        if self.is_reminder_set.get():
            self.text_color.set('black')
            self.max_months.set(12)
        else:
            self.text_color.set('grey')
            self.max_months.set(0)
            self.months.configure(textvariable='')
        self.months.configure(to=self.max_months.get())
        self.reminder_label.configure(foreground=self.text_color.get())

    def save_settings(self, controller):
        if controller.is_admin:
            self.months_set.set(self.months.get())
            self.limit.set(self.limit_entry.get())
            self.controller.show_frame('HomePage')
        else:
            tm.showerror("Error!", "You have no permissions to change settings!")

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.is_reminder_set = BooleanVar()
        self.text_color = StringVar()
        self.text_color.set('grey')
        self.max_months = IntVar()
        self.max_months.set(0)
        self.months_set = IntVar()
        self.limit = IntVar()

        self.background_img = PhotoImage(file="resources/background.gif")
        self.back_img = PhotoImage(file="resources/back.gif")

        settings_canvas = Canvas(self, width=1280, height=720)
        settings_canvas.pack(side='top', fill='x')
        self.settings_label = Label(self, width=130, height=30)
        self.settings_label.place(x=190, y=110)

        settings_canvas.create_image(640, 360, image=self.background_img)
        settings_canvas.create_text(640, 60, fill='blue', font="Times 40 bold", text='Settings')

        settings_canvas.create_image(100, 60, image=self.back_img, tag='back')
        settings_canvas.tag_bind('back', '<Button-1>', lambda event: controller.show_frame('HomePage'))

        Label(self.settings_label, font="Times 20 bold", text='Set up reminder').place(x=200, y=50)

        self.reminder = Checkbutton(self.settings_label, width=1, variable=self.is_reminder_set,
                                    command=lambda: self.set_reminder(), onvalue=True, offvalue=False)
        self.reminder.place(x=400, y=59)

        self.reminder_label = Label(self.settings_label, foreground=self.text_color.get(), font="Times 20 bold",
                                    text='Remind upcoming ending of a product          months before')
        self.reminder_label.place(x=120, y=110)
        self.months = Spinbox(self.settings_label, from_=0, to=self.max_months.get(), width=3, font='Helvetica 14 bold')
        self.months.place(x=580, y=118)

        Label(self.settings_label, font="Times 20 bold", text='Limit at the given month: ').place(x=200, y=170)
        self.limit_entry = Entry(self.settings_label, bd=5, font='Helvetica 14 bold')
        self.limit_entry.place(x=510, y=168, width=100)
        Label(self.settings_label, font="Times 20 bold", text='€').place(x=620, y=170)

        save_btn = Button(settings_canvas, text="Save", font="Times 20 bold",
                          command=lambda: self.save_settings(controller))
        save_btn.place(x=600, y=620)


class HelpPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

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
        help_label.tag_bind('back', '<Button-1>', lambda event: controller.show_frame('HomePage'))


if __name__ == "__main__":
    app = InventoryPlanner()
    app.mainloop()
