from tkinter import *
from tkinter import messagebox
from checkbar import CheckBar
import json
check_box = []
labels = []
user_nam = ''


class User:
    def __init__(self, window, canvas, c1, c2, c3):
        self.window6 = None
        self.canvas = canvas
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.user_log = Button(window, text="Login", width=15, fg="White", bg="black", highlightthickness=0,
                               command=self.user_login)
        self.button2 = Button(window, text="Register", width=15, fg="White", bg="black", highlightthickness=0,
                              command=self.register)

        self.place_order = Button(window, text="Place new order", width=15, fg="White", bg="black",
                                  highlightthickness=0, command=self.place_order)
        self.order_history = Button(window, text="Order History", width=15, fg="White", bg="black",
                                    highlightthickness=0)
        self.update_profile = Button(window, text="Update Profile", width=15, fg="White", bg="black",
                                     highlightthickness=0, command=self.update_prof)

        self.user_name = Label(window, text="User Name :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.entry = Entry(width=50)
        self.entry.focus()
        self.password = Label(window, text="Password :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.pass_entry = Entry(width=50)

    def user_login(self):
        global user_nam
        user_nam = self.entry.get()
        user_pass = self.pass_entry.get()
        with open("data_user.json", "r+") as fp:
            data = json.load(fp)
        if user_nam in data:
            if user_pass == data[user_nam]['Password']:
                self.user_log.destroy()
                self.button2.destroy()
                self.user_name.destroy()
                self.entry.destroy()
                self.password.destroy()
                self.pass_entry.destroy()
                self.display_user()
            else:
                messagebox.showerror("OOPS!!", "Entered password is Incorrect")
        else:
            messagebox.showerror("OOPS!!", "User name doesn't exist. Please register")

    def user_save_details(self, user_n):
        full_n = self.full_entry.get()
        phone_number = self.phone_entry.get()
        email_1 = self.email_entry.get()
        address_1 = self.address_entry.get("1.0", END)
        password_1 = self.password_entry.get()

        new_data = {user_n: {
            "Full Name": full_n,
            "Phone Number": phone_number,
            "Email": email_1,
            "Address": address_1,
            "Password": password_1
        }
        }
        if user_n != '' and full_n != '' and phone_number != '' and email_1 != '' \
                and address_1 != '' and password_1 != "":
            is_ok = messagebox.askokcancel("User Details", f"Are you sure entered details are correct ?")
            if is_ok:
                try:
                    with open('data_user.json', 'r+') as fp:
                        data = json.load(fp)
                        data.update(new_data)
                except json.decoder.JSONDecodeError:
                    with open('data_user.json', 'w') as fp:
                        json.dump(new_data, fp, indent=4)
                except FileNotFoundError:
                    with open('data_user.json', 'w') as fp:
                        json.dump(new_data, fp, indent=4)
                else:
                    with open('data_user.json', 'w') as fp:
                        json.dump(data, fp, indent=4)
                self.window6.destroy()
                messagebox.showinfo('information', "Saved successfully")

        else:
            self.window6.destroy()
            messagebox.showerror("Error", "Please don't leave any of fields empty")

    def save_details(self):
        with open("data_user.json", "r+") as fp1:
            data2 = json.load(fp1)
        try:
            user_n = self.user_entry1.get()
            if user_n in data2:
                messagebox.showerror("OOPS!!", "Entered user name already exists")
            else:
                self.user_save_details(user_n)
        except TclError:
            user_n = user_nam
            self.user_save_details(user_n)

    def register(self):
        self.window6 = Tk()
        self.window6.title("User Details")
        self.window6.config(padx=50, pady=50)
        self.user_label = Label(self.window6, text=user_nam)
        self.user_name = Label(self.window6, text="User name :")
        self.user_name.grid(column=0, row=0)
        self.user_entry1 = Entry(self.window6, width=30)
        self.user_entry1.grid(column=1, row=0)
        self.user_entry1.focus()
        self.full_name = Label(self.window6, text="Full name :")
        self.full_name.grid(column=0, row=1)
        self.full_entry = Entry(self.window6, width=30)
        self.full_entry.grid(column=1, row=1)
        self.phone_num = Label(self.window6, text="Phone Number :")
        self.phone_num.grid(column=0, row=2)
        self.phone_entry = Entry(self.window6, width=30)
        self.phone_entry.grid(column=1, row=2)
        self.email = Label(self.window6, text="Email :")
        self.email.grid(column=0, row=3)
        self.email_entry = Entry(self.window6, width=30)
        self.email_entry.grid(column=1, row=3)
        self.address = Label(self.window6, text="Address :")
        self.address.grid(column=0, row=4)
        self.address_entry = Text(self.window6, height=4, width=22)
        self.address_entry.grid(column=1, row=4)
        self.password = Label(self.window6, text="Password :")
        self.password.grid(column=0, row=5)
        self.password_entry = Entry(self.window6, width=30)
        self.password_entry.grid(column=1, row=5)
        self.save = Button(self.window6, text="Save User", width=20, command=self.save_details)
        self.save.grid(column=1, row=6)

    def display_user(self):
        self.canvas.delete(self.c1)
        self.canvas.delete(self.c2)
        self.canvas.moveto(self.c3, x=300, y=30)
        self.canvas.create_text(720, 100, text=f"Logged in as {user_nam}")
        self.place_order.place(x=400, y=250)
        self.order_history.place(x=600, y=250)
        self.update_profile.place(x=500, y=300)

    def update_prof(self):
        global user_nam
        with open("data_user.json", "r+") as fp:
            data1 = json.load(fp)
        full_nam = data1[user_nam]["Full Name"]
        phone_n = data1[user_nam]["Phone Number"]
        email_us = data1[user_nam]["Email"]
        address = data1[user_nam]["Address"]
        pass_use = data1[user_nam]["Password"]
        self.register()
        self.user_entry1.destroy()
        self.user_label.grid(column=1, row=0)
        self.full_entry.insert(END, full_nam)
        self.phone_entry.insert(END, phone_n)
        self.email_entry.insert(END, email_us)
        self.address_entry.insert(END, address)
        self.password_entry.insert(END, pass_use)

    def place_order(self):
        global labels, check_box

        def order_placed():
            d = list(check.state())
            print(d)
        window2 = Tk()
        window2.title("List of items")
        window2.config(padx=50, pady=50)
        l0 = Label(window2, text="Select item")
        l1 = Label(window2, text="Food ID")
        l2 = Label(window2, text="Name")
        l3 = Label(window2, text="Quantity")
        l4 = Label(window2, text="Price")
        l5 = Label(window2, text="Discount in %")
        l6 = Label(window2, text="Final Price")
        l7 = Label(window2, text="Stock Left")
        order_place = Button(window2, text="Place Order", command=order_placed)
        back = Button(window2, text='Back', command=window2.destroy)
        with open("data.json", 'r') as fp:
            data = json.load(fp)
        l0.grid(column=0, row=0)
        l1.grid(column=1, row=0)
        l2.grid(column=2, row=0)
        l3.grid(column=3, row=0)
        l4.grid(column=4, row=0)
        l5.grid(column=5, row=0)
        l6.grid(column=6, row=0)
        l7.grid(column=7, row=0)

        item_id = []
        item_name = []
        item_qua = []
        item_price = []
        item_discount = []
        item_final_price = []
        item_stock = []

        for i in range(len(data)):
            data_1 = data.keys()
            data_2 = list(data_1)
            item_1 = data_2[i]
            item_id.append(item_1)
            item_name.append(data[item_1]["Name"])
            item_qua.append(data[item_1]["Quantity"])
            item_price.append(data[item_1]["Price"])
            item_discount.append(data[item_1]["Discount"])
            item_final_price.append(data[item_1]["FinalPrice"])
            item_stock.append(data[item_1]["stockLeft"])

            food_num = Label(window2, text=item_id[i])
            food_num.grid(column=1, row=i + 1)

            food_name = Label(window2, text=item_name[i])
            food_name.grid(column=2, row=i + 1, sticky='W')

            food_qua = Label(window2, text=item_qua[i])
            food_qua.grid(column=3, row=i + 1)

            food_price = Label(window2, text=item_price[i])
            food_price.grid(column=4, row=i + 1)

            food_discount = Label(window2, text=item_discount[i])
            food_discount.grid(column=5, row=i + 1)

            food_final_price = Label(window2, text=item_final_price[i])
            food_final_price.grid(column=6, row=i + 1)

            food_stock = Label(window2, text=item_stock[i])
            food_stock.grid(column=7, row=i + 1)

            labels.append([ food_num, food_name, food_qua, food_price, food_discount,
                           food_final_price, food_stock])
        print(item_id)
        check = CheckBar(window2, item_id)
        order_place.grid(column=8, row=len(data)+2)
        back.grid(column=8, row=len(data) + 3)
        window2.mainloop()


