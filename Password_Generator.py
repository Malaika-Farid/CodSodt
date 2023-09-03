import tkinter as tk
import string
import random

# Function to generate a random password
def generate_password():
    password_length = int(length_entry.get())
    if password_length <= 0:
        password_label.config(text="Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create and place widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack(pady=10)

# Start the main loop
root.mainloop()
