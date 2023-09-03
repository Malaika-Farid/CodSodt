import tkinter as tk
from tkinter import ttk

# Function to update the display
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Creating a custom font
font = ("Helvetica", 20)

# Entry widget for display
entry = tk.Entry(root, font=font, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10, sticky="nsew")

# Defining calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Creating style for buttons
button_style = ttk.Style()
button_style.configure("TButton", font=font, padding=10)

# Creating buttons and place them in the grid
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        ttk.Button(root, text=button, padding=20, command=calculate, style="TButton").grid(row=row_val, column=col_val, sticky="nsew")
    else:
        ttk.Button(root, text=button, padding=20, command=lambda b=button: button_click(b), style="TButton").grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configuration of row and column weights to make the buttons expand with the window
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)

# Starts the main loop
root.mainloop()