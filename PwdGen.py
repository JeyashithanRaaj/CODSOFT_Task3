import tkinter as tk
import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        characters = string.ascii_letters + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper()
    else:
        raise ValueError("Invalid complexity level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_button_clicked():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    password = generate_password(length, complexity)
    
    result_label.config(text="Generated Password:\n" + password)

root = tk.Tk()
root.title("Password Generator")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

length_label = tk.Label(frame, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

length_entry = tk.Entry(frame)
length_entry.grid(row=0, column=1, padx=10, pady=10)

complexity_label = tk.Label(frame, text="Password Complexity:")
complexity_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

complexity_var = tk.StringVar()
complexity_var.set("medium")

low_complexity_radio = tk.Radiobutton(frame, text="Low", variable=complexity_var, value="low")
medium_complexity_radio = tk.Radiobutton(frame, text="Medium", variable=complexity_var, value="medium")
high_complexity_radio = tk.Radiobutton(frame, text="High", variable=complexity_var, value="high")

low_complexity_radio.grid(row=1, column=1, padx=10, pady=10, sticky="w")
medium_complexity_radio.grid(row=1, column=2, padx=10, pady=10, sticky="w")
high_complexity_radio.grid(row=1, column=3, padx=10, pady=10, sticky="w")

generate_button = tk.Button(frame, text="Generate Password", command=generate_button_clicked)
generate_button.grid(row=2, columnspan=4, padx=10, pady=20)

result_label = tk.Label(frame, text="Generated Password will appear here.")
result_label.grid(row=3, columnspan=4, padx=10, pady=10)

root.mainloop()
