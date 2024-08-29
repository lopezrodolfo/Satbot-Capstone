import tkinter as tk

# Create a new window
window = tk.Tk()

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "myusername" and password == "mypassword":
        message_label.config(text="Login successful!")
    else:
        message_label.config(text="Incorrect username or password")



window.geometry("500x500")
window.title("Login")

# create username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

#create label and entry for password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# create message label
message_label = tk.Label(root, text="")
message_label.pack()

# Create a button
#button = tk.Button(window, text="Click me!", command=lambda: print("Button clicked!"))

# Add the label and button to the window
#label.pack(pady=10)
#button.pack()

# Run the GUI
window.mainloop()
