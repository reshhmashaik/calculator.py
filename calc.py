import tkinter as tk

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            entry_var.set(eval(entry_var.get()))
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons, 1):
    for c, button_text in enumerate(row):
        tk.Button(root, text=button_text, font=("Arial", 20), command=lambda b=button_text: on_click(b)).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
