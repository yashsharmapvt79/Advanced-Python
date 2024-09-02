import tkinter as tk

def click(event):
    current = entry.get()
    if event.widget.cget("text") == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif event.widget.cget("text") == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, event.widget.cget("text"))

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Corrected buttons list
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0, 4)  # This button spans 4 columns
]

for item in buttons:
    if len(item) == 4:
        text, row, col, colspan = item
        button = tk.Button(root, text=text, width=4, height=2)
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew")
    else:
        text, row, col = item
        button = tk.Button(root, text=text, width=4, height=2)
        button.grid(row=row, column=col, sticky="nsew")

    button.bind('<Button-1>', click)

# Adjust column and row weights
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
