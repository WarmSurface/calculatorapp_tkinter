import tkinter as tk #calculator app Date:16/06/2023

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_del():
    display.delete(len(display.get())-1) 

calc = tk.Tk()
calc.title("Calculator")

display = tk.Entry(calc, width=20, font=("Arial", 22))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(calc, text=button_text, width=5, font=("Arial", 14),background="gray", command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5)

eqaul_button = tk.Button(calc,text="=",width=5,font=("Arial",14), command=button_equal)
eqaul_button.grid(row=4,column=2,padx=5,pady=5)

clear_button = tk.Button(calc, text="C", width=5, font=("Arial", 14), background="blue", command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

del_button = tk.Button(calc, text="DEL", width=5, font=("Arial", 14),background="red", command=button_del)
del_button.grid(row=5, column=1, padx=5, pady=5)

Credits = tk.Label(calc, text="WarmSurface", font=("Courier", 14))
Credits.grid(row=6, column=3, padx=5, pady=5)

calc.mainloop()