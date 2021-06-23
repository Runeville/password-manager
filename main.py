from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password = generate_password()
    password_entry.delete(0, 99999)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website != '' and password != '' and email != '':
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except:
            with open("passwords.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("passwords.json", 'w') as file:
                json.dump(data, file, indent=4)

    else:
        messagebox.showwarning(title='Warning', message='All entries must be filled')


# ---------------------------- Searching website ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            data = data[website]
            print(data)
            messagebox.showinfo(website, f'Email: {data["email"]} \nPassword: {data["password"]}')
    except:
        messagebox.showinfo(website, 'Nothing found')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg='white')
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", bg='white')
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", bg='white')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, padx=20, sticky=W)

email_entry = Entry(width=60)
email_entry.grid(column=1, row=2, columnspan=2, padx=20, sticky=W)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, padx=20, sticky=W)

# Buttons
search_button = Button(text='Search', width=15, command=search)
search_button.grid(column=2, row=1, sticky=W)

generate_password_button = Button(text='Generate Password', command=generate)
generate_password_button.grid(column=2, row=3, sticky=W)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
