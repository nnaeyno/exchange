import tkinter as tk
from tkinter import messagebox


def clear_field_and_show_input():
    input_text = entry.get()
    selected_currency_1 = from_curr.get()
    selected_currency_2 = to_curr.get()

    if is_valid_number(input_text):
        label_display.config(text=f"Calculated amount: {input_text} {selected_currency_2}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number (integer or float).")


def is_valid_number(input_text):
    try:
        float(input_text)
        return True
    except ValueError:
        return False


def create_drop_down(input_frame):
    currency_var = tk.StringVar(value="$")
    currency_dropdown = tk.OptionMenu(input_frame, currency_var, "$", "€")
    currency_dropdown.pack(side=tk.LEFT)
    return currency_var


root = tk.Tk()
root.title("Clear Field App")
root.geometry("450x300")

input_frame = tk.Frame(root)
input_frame.pack(pady=20)

tk.Label(input_frame, text="From:").pack(side=tk.LEFT, padx=5)

from_curr = create_drop_down(input_frame)

entry = tk.Entry(input_frame, width=15)
entry.pack(side=tk.LEFT, padx=5)

tk.Label(input_frame, text="To:").pack(side=tk.LEFT, padx=5)

to_curr = create_drop_down(input_frame)

clear_button = tk.Button(root, text="Clear & Show Input", command=clear_field_and_show_input)
clear_button.pack(pady=10)

label_display = tk.Label(root, text="", font=("Helvetica", 14))
label_display.pack(pady=10)

root.mainloop()
