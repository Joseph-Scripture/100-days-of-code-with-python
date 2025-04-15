from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import json
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            'email': email,
            'password': password
        }                     
    }






    if len(website) ==0 or len(password) ==0 :
        messagebox.showinfo(title="OOPS", message="Please make sure you haven't left any fields empty")

    else:   
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                data = json.dump(new_data, indent=4)
            # Reading from json file
        else:
            # updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving data to the json file
                json.dump(data, data_file, indent= 4)
        finally:    
            website_entry.delete(0, END)
        password_entry.delete(0, END)
def search_function():
    
    website = website_entry.get()
    
    try: 
        with open("data.json") as data_file:
            # data = json.load(data_file)
            data = json.load(data_file)


    except FileNotFoundError:
        messagebox.showinfo(title='Error', message= 'No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website['password']]
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f"No details for  {website} exists")




    # try:
    #     with open('data.json', 'r') as data_file:
    #         data = json.load(data_file)
    # except FileNotFoundError:
    #     with open('data.json', 'w') as data_file:
    #         data = json.dump(new_data)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

password_image = PhotoImage(file='logo.png',)
canvas = Canvas(width=200, height=200, highlightthickness=0 )
canvas.create_image(100, 100 ,image = password_image,  )
canvas.grid(row=0, column=1)



website_label = Label(width=36, text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(width=36, text='Username/Email:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'scripture2@yahoo.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)




generate_password_button = Button(text='Generate Password', command=password_generate)
generate_password_button.grid(column=2 ,row=3)
add_button = Button(text='Add', width=36,command=save)
add_button.grid(row=4, column=1, columnspan=2)


searc_button = Button(text='Search', command= search_function)
searc_button.grid(column=2, row=1)










window.mainloop()

