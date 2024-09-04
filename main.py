import tkinter as tk
from tkinter import messagebox

import currency_calculator


def clear_action():
    entry.delete(0, tk.END)
    label_display.config(
        text="")
    from_curr.set(all_codes[0])
    to_curr.set(all_codes[0])


def convert_action():
    amount = entry.get()
    if is_valid_number(amount):
        from_value = from_curr.get()
        to_value = to_curr.get()
        converted_amount = currency_calculator.convert_and_display(from_value, to_value, amount)
        label_display.config(
            text=f"{amount} {from_value} = {converted_amount:.2f} {to_value}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number (integer or float).")


def is_valid_number(input_text):
    try:
        float(input_text)
        return True
    except ValueError:
        return False


def create_drop_down(frame):
    currency_var = tk.StringVar(value=all_codes[0])
    currency_dropdown = tk.OptionMenu(frame, currency_var, *all_codes)
    currency_dropdown.pack(side=tk.LEFT)
    return currency_var


root = tk.Tk()
root.title("Currency converter")
root.geometry("450x300")

input_frame = tk.Frame(root)
input_frame.pack(pady=20)

tk.Label(input_frame, text="From:").pack(side=tk.LEFT, padx=5)
all_codes = currency_calculator.get_currencies_codes()

from_curr = create_drop_down(input_frame)

entry = tk.Entry(input_frame, width=15)
entry.pack(side=tk.LEFT, padx=5)

tk.Label(input_frame, text="To:").pack(side=tk.LEFT, padx=5)

to_curr = create_drop_down(input_frame)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

convert_button = tk.Button(button_frame, text="Convert", command=convert_action)
convert_button.pack(side=tk.LEFT, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear_action)
clear_button.pack(side=tk.LEFT, padx=5)

label_display = tk.Label(root, text="", font=("Helvetica", 14))
label_display.pack(pady=10)

root.mainloop()
