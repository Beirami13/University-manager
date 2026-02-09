from tkinter import *

root = Tk()
root.title('Calculate')
root.geometry('300x250')
root.resizable(False, False)

typed_numbers = ""

display = Entry(root)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=5, ipady=10)

result_var = StringVar()
result_label = Label(root, textvariable=result_var, background="grey")
result_label.grid(row=0, column=5, padx=10, pady=5)

def add_number(num):
    display.insert(END, num)

def press(key):
    display.insert(END, key)

def calculate():
    text = display.get()
    result=eval(text)
    display.delete(0, END)
    display.insert(END, result)


Button(root, text="          +          ", command=lambda: press("+")).grid(row=1, column=1, padx=10, pady=5)
Button(root, text="          -          ", command=lambda: press("-")).grid(row=1, column=3, padx=10, pady=5)
Button(root, text="          *          ", command=lambda: press("*")).grid(row=1, column=5, padx=10, pady=5)
Button(root, text="          /          ", command=lambda: press("/")).grid(row=2, column=1, padx=10, pady=5)
Button(root, text="          =          ", command=calculate).grid(row=2, column=5, padx=10, pady=5)

Button(root, text="          0          ", command=lambda: press("0")).grid(row=2, column=3, padx=10, pady=5)
Button(root, text="          1          ", command=lambda: press("1")).grid(row=3, column=1, padx=10, pady=5)
Button(root, text="          2          ", command=lambda: press("2")).grid(row=3, column=3, padx=10, pady=5)
Button(root, text="          3          ", command=lambda: press("3")).grid(row=3, column=5, padx=10, pady=5)
Button(root, text="          4          ", command=lambda: press("4")).grid(row=4, column=1, padx=10, pady=5)
Button(root, text="          5          ", command=lambda: press("5")).grid(row=4, column=3, padx=10, pady=5)
Button(root, text="          6          ", command=lambda: press("6")).grid(row=4, column=5, padx=10, pady=5)
Button(root, text="          7          ", command=lambda: press("7")).grid(row=5, column=1, padx=10, pady=5)
Button(root, text="          8          ", command=lambda: press("8")).grid(row=5, column=3, padx=10, pady=5)
Button(root, text="          9          ", command=lambda: press("9")).grid(row=5, column=5, padx=10, pady=5)

root.mainloop()
