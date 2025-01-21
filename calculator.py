import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Main Tkinter window
window = tk.Tk()
window.title("Calculator")

# Entry field
entry = tk.Entry(window, width=20, font=('Arial', 18), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=button_equal)
    elif text == 'C':
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=button_clear)
    else:
        button = tk.Button(window, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew")

# Adjust row and column weights
for i in range(5):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

# Run the Tkinter event loop
window.mainloop()
