from tkinter import *
from tkinter import messagebox
import json

labels = []


class Admin:
    def __init__(self, window, canvas, c1, c2, c3):
        self.canvas = canvas
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.user_name = Label(window, text="User Name :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.entry = Entry(width=50)
        self.entry.focus()
        self.password = Label(window, text="Password :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.pass_entry = Entry(width=50)
        self.login = Button(window, text="Login", fg="white", bg="black", highlightthickness=0,
                            width=10, command=self.admin_login)

        self.add = Button(window, text="Add item", fg="white", bg="black", highlightthickness=0,
                          width=15, command=self.add_item)
        self.view = Button(window, text="View items", width=15, fg="white", bg="black", highlightthickness=0,
                           command=self.view_list)
        self.edit = Button(window, text='Edit items', fg="white", bg="black", highlightthickness=0,
                            width=15, command=self.edit_item)
        self.remove = Button(window, text="Remove item", width=15,fg="white", bg="black", highlightthickness=0,
                             command=self.remove_item)

    def admin_login(self):
        self.user_name.destroy()
        self.entry.destroy()
        self.password.destroy()
        self.pass_entry.destroy()
        self.login.destroy()

        self.canvas.delete(self.c1)
        self.canvas.delete(self.c2)
        self.canvas.moveto(self.c3, x=300, y=30)
        self.canvas.create_text(720, 100, text="Logged in as admin")

        self.add.place(x=400, y=200)
        self.view.place(x=550, y=200)
        self.edit.place(x=400, y=300)
        self.remove.place(x=550, y=300)

    @staticmethod
    def add_item():
        with open("data.json", "r") as fp:
            data = json.load(fp)
        num = len(data)
        food_id = f"I{num}"
        if food_id in data:
            food_id = f"I{num + 1}"

        def save_item():
            food_num = id_entry.get()
            if food_num in data:
                messagebox.showinfo("OOPS!!", "Food id already exists")
            else:
                food_name = name_entry.get()
                food_qua = qua_entry.get() + " gms"
                food_price = price_entry.get()
                food_discount = disc_entry.get()
                if food_discount == 0 or food_discount == '':
                    food_fp = food_price
                else:
                    food_fp = int(food_price) - (int(food_price) / int(food_discount))
                food_stock = stock_entry.get() + " gms"

                new_data = {food_num: {
                    "Name": food_name,
                    "Quantity": food_qua,
                    "Price": food_price,
                    "Discount": food_discount,
                    "FinalPrice": food_fp,
                    "stockLeft": food_stock
                },
                }
                if food_num == '' or food_name == "" or food_qua == '' or food_price == '' or food_stock == '':
                    messagebox.showinfo('OOPS!!', "Enter all required details.")
                else:
                    with open("data.json", "r+") as fp1:
                        data1 = json.load(fp1)
                        data1.update(new_data)
                    with open("data.json", "w") as fp1:
                        json.dump(data1, fp1, indent=4)
                    messagebox.showinfo('information', "Added successfully")
            window3.destroy()

        window3 = Tk()
        window3.title("Add item")
        window3.config(padx=100, pady=100)

        id_food = Label(window3, text="Food id :")
        id_food.grid(column=0, row=0)

        id_entry = Entry(window3, width=30)
        id_entry.insert(END, food_id)
        id_entry.grid(column=1, row=0)

        name_food = Label(window3, text="Food Name :")
        name_food.grid(column=0, row=1)

        name_entry = Entry(window3, width=30)
        name_entry.grid(column=1, row=1)
        name_entry.focus()

        qua_food = Label(window3, text="Quantity in gms :")
        qua_food.grid(column=0, row=2)

        qua_entry = Entry(window3, width=30)
        qua_entry.grid(column=1, row=2)

        price_food = Label(window3, text="Price :")
        price_food.grid(column=0, row=3)

        price_entry = Entry(window3, width=30)
        price_entry.grid(column=1, row=3)

        disc_food = Label(window3, text="Discount in %:")
        disc_food.grid(column=0, row=4)

        disc_entry = Entry(window3, width=30)
        disc_entry.grid(column=1, row=4)

        stock_food = Label(window3, text="Stock Left in gms:")
        stock_food.grid(column=0, row=6)

        stock_entry = Entry(window3, width=30)
        stock_entry.grid(column=1, row=6)

        save = Button(window3, text="Save", width=45, command=save_item)
        save.grid(column=0, row=7, columnspan=2)

        back = Button(window3, text='Back', command=window3.destroy, width=45)
        back.grid(column=0, row=8, columnspan=2)

    @staticmethod
    def view_list():
        global labels
        window2 = Tk()
        window2.title("List of items")
        window2.minsize(width=1000, height=600)
        l1 = Label(window2, text="Food ID")
        l2 = Label(window2, text="Name")
        l3 = Label(window2, text="Quantity")
        l4 = Label(window2, text="Price")
        l5 = Label(window2, text="Discount in %")
        l6 = Label(window2, text="Final Price")
        l7 = Label(window2, text="Stock Left")
        back = Button(window2, text='Back', command=window2.destroy)
        with open("data.json", 'r') as fp:
            data = json.load(fp)
        l1.grid(column=0, row=0)
        l2.grid(column=1, row=0)
        l3.grid(column=2, row=0)
        l4.grid(column=3, row=0)
        l5.grid(column=4, row=0)
        l6.grid(column=5, row=0)
        l7.grid(column=6, row=0)

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
            food_num.grid(column=0, row=i + 1)

            food_name = Label(window2, text=item_name[i])
            food_name.grid(column=1, row=i + 1, sticky='W')

            food_qua = Label(window2, text=item_qua[i])
            food_qua.grid(column=2, row=i + 1)

            food_price = Label(window2, text=item_price[i])
            food_price.grid(column=3, row=i + 1)

            food_discount = Label(window2, text=item_discount[i])
            food_discount.grid(column=4, row=i + 1)

            food_final_price = Label(window2, text=item_final_price[i])
            food_final_price.grid(column=5, row=i + 1)

            food_stock = Label(window2, text=item_stock[i])
            food_stock.grid(column=6, row=i + 1)

            labels.append([food_num, food_name, food_qua, food_price, food_discount, food_final_price, food_stock])
        back.grid(column=8, row=len(data) + 3)
        window2.mainloop()

    @staticmethod
    def edit_item():
        def enter_details():
            with open("data.json", "r+") as fp:
                data = json.load(fp)
            food_number = take_entry.get()
            if food_number not in data:
                messagebox.showinfo("OOPS!!", "Entered food id doesn't exists")
            else:
                take_id.destroy()
                take_entry.destroy()
                enter.destroy()
                name = data[food_number]["Name"]
                qua = data[food_number]["Quantity"]
                price = data[food_number]["Price"]
                disc = data[food_number]["Discount"]
                stock = data[food_number]["stockLeft"]

                id_food = Label(window4, text="Food id :")
                id_food.grid(column=0, row=0)

                id_entry = Label(window4, text=food_number, width=30)
                id_entry.grid(column=1, row=0)

                name_food = Label(window4, text="Food Name :")
                name_food.grid(column=0, row=1)

                name_entry = Entry(window4, width=30)
                name_entry.insert(END, name)
                name_entry.grid(column=1, row=1)

                qua_food = Label(window4, text="Quantity in gms :")
                qua_food.grid(column=0, row=2)

                qua_entry = Entry(window4, width=30)
                qua_entry.insert(END, qua)
                qua_entry.grid(column=1, row=2)

                price_food = Label(window4, text="Price :")
                price_food.grid(column=0, row=3)

                price_entry = Entry(window4, width=30)
                price_entry.insert(END, price)
                price_entry.grid(column=1, row=3)

                disc_food = Label(window4, text="Discount in %:")
                disc_food.grid(column=0, row=4)

                disc_entry = Entry(window4, width=30)
                disc_entry.insert(END, disc)
                disc_entry.grid(column=1, row=4)

                stock_food = Label(window4, text="Stock Left in gms:")
                stock_food.grid(column=0, row=6)

                stock_entry = Entry(window4, width=30)
                stock_entry.insert(END, stock)
                stock_entry.grid(column=1, row=6)

                def save_details():
                    food_num = food_number
                    food_name = name_entry.get()
                    food_qua = qua_entry.get()
                    food_price = price_entry.get()
                    food_discount = disc_entry.get()
                    if food_discount == 0 or food_discount == '':
                        food_fp = food_price
                    else:
                        food_fp = int(food_price) - (int(food_price) / int(food_discount))
                    food_stock = stock_entry.get()

                    new_data = {food_num: {
                        "Name": food_name,
                        "Quantity": food_qua,
                        "Price": food_price,
                        "Discount": food_discount,
                        "FinalPrice": food_fp,
                        "stockLeft": food_stock
                    },
                    }
                    if food_num == '' or food_name == "" or food_qua == '' or food_price == '' or food_stock == '':
                        messagebox.showinfo('OOPS!!', "Enter all required details.")
                    else:
                        with open("data.json", "r+") as fp1:
                            data1 = json.load(fp1)
                            data1.update(new_data)
                        with open("data.json", "w") as fp1:
                            json.dump(data1, fp1, indent=4)
                            messagebox.showinfo('information', "Saved successfully")
                    window4.destroy()

                save = Button(window4, text="Save", width=15, command=save_details)
                save.grid(column=1, row=7, columnspan=2)

                back = Button(window4, text="Back", width=15, command=window4.destroy)
                back.grid(column=1, row=8, columnspan=2)

        window4 = Tk()
        window4.title("Edit item")
        window4.config(padx=100, pady=100)
        take_id = Label(window4, text=" Enter food id to edit :")
        take_id.grid(column=0, row=0)

        take_entry = Entry(window4, width=25)
        take_entry.grid(column=1, row=0)

        enter = Button(window4, text="Enter", width=15, command=enter_details)
        enter.grid(column=1, row=1)

        window4.mainloop()

    @staticmethod
    def remove_item():
        def remove_food():
            food_number = take_entry.get()

            with open("data.json", "r+") as fp:
                data = json.load(fp)
            if food_number in data:
                is_ok = messagebox.askokcancel("Confirmation", f"Are you sure to remove {food_number} item from data ?")
                if is_ok:
                    del data[food_number]
                    new_data = data
                    with open("data.json", "w+") as fp1:
                        json.dump(new_data, fp1, indent=4)
                    messagebox.showinfo("Info", f"{food_number} item was removed successfully")
            else:
                messagebox.showinfo("OOPs!!", "Entered id is not there in data")
            window5.destroy()

        window5 = Tk()
        window5.title("Remove Item")
        window5.config(padx=100, pady=100)
        take_id = Label(window5, text=" Enter food id to remove :")
        take_id.grid(column=0, row=0)

        take_entry = Entry(window5, width=25)
        take_entry.grid(column=1, row=0)

        remove_but = Button(window5, text="Remove", width=15, command=remove_food)
        remove_but.grid(column=1, row=1)

        window5.mainloop()
