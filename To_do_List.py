import tkinter as tk

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to remove a selected task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place task entry widget
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Create and place Add and Remove buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
remove_button.pack()

# Create and place the task listbox
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()