from tkinter import *
from admin import Admin
from user import User

user_nam = ''


def del_button():
    button1.destroy()
    button.destroy()
    admin_1.user_name.place(x=300, y=300)
    admin_1.entry.place(x=420, y=305)
    admin_1.password.place(x=300, y=350)
    admin_1.pass_entry.place(x=420, y=355)
    admin_1.login.place(x=450, y=405)


def user_button():
    button1.destroy()
    button.destroy()
    user_1.user_name.place(x=300, y=300)
    user_1.entry.place(x=420, y=305)
    user_1.password.place(x=300, y=350)
    user_1.pass_entry.place(x=420, y=355)
    user_1.user_log.place(x=450, y=405)
    user_1.button2.place(x=600, y=405)


window = Tk()
window.title("Hotel - Marasasarovar")
window.minsize(width=800, height=600)
window.config(bg="#f1ddbf")

canvas = Canvas(width=800, height=600, highlightthickness=0)
bg_img = PhotoImage(file='bg3.png')
canvas.create_image(400, 300, image=bg_img)
c1 = canvas.create_text(490, 30, text='Welcome', fill='#06113C', font=("Arial", 30, 'bold'))
c2 = canvas.create_text(490, 75, text='to', fill='#06113C', font=("Arial", 30, 'bold'))
c3 = canvas.create_text(490, 120, text='Hotel - Marasasarovar', fill='#06113C', font=("Arial", 30, 'bold'))
canvas.place(x=0, y=0)

button = Button(text="Login as admin", fg="white", bg="black", highlightthickness=0, command=del_button)
button.place(x=350, y=300)

button1 = Button(text="Login as User", fg="white", bg="black", highlightthickness=0, command=user_button)
button1.place(x=600, y=300)

admin_1 = Admin(window, canvas, c1, c2, c3)
user_1 = User(window, canvas, c1, c2, c3)

window.mainloop()
