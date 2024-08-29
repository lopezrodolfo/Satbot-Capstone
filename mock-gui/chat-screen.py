import tkinter as tk


root = tk.Tk()
root.title("SatBot")
root.geometry("900x700")
label_font = ("Times New Roman", 16, "bold")

# Create a text widget to display the chat history
chat_history = tk.Text(root, width=60, height=40)
chat_history.pack()

# Create a label and an entry widget for the user to type messages
message_label = tk.Label(root, text="Enter message:", font=label_font,fg="blue")

message_label.pack()

message_entry = tk.Entry(root, width=30)
message_entry.pack()

# Create a function to handle sending messages
def send_message():
    # Get the message from the entry widget
    message = message_entry.get()
    
    # Add the message to the chat history
    chat_history.insert(tk.END, "You: " + message + "\n")
    
    # Clear the message entry widget
    message_entry.delete(0, tk.END)
    
    # Send a response 
    chat_history.insert(tk.END, "")

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send_message, fg="blue")
send_button.pack()

# Run the main event loop
root.mainloop()
