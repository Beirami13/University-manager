from tkinter import *
import math

root = Tk()
root.title('Calculate')
root.geometry('400x250')
root.resizable(False, False)

display = Entry(root, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=10, padx=5, pady=10, ipadx=5, ipady=5)

def add_number(num):
    display.insert(END, num)

def press(key):
    display.insert(END, key)

def calculate():
    text = display.get()
    text = text.replace("^", "**")

    try:
        result = eval(text, {"__builtins__": None}, math.__dict__)
    except:
        result = "Error"

    display.delete(0, END)
    display.insert(END, result)


def clear():
    display.delete(0, END)

def back():
    text = display.get()
    new_text = text[:-1]
    display.delete(0, END)
    display.insert(END, new_text)

Button(root, text="          +          ", command=lambda: press("+")).grid(row=1, column=1, padx=10, pady=5)
Button(root, text="          -          ", command=lambda: press("-")).grid(row=1, column=3, padx=10, pady=5)
Button(root, text="          *          ", command=lambda: press("*")).grid(row=1, column=5, padx=10, pady=5)
Button(root, text="          /          ", command=lambda: press("/")).grid(row=2, column=1, padx=10, pady=5)
Button(root, text="          ^          ", command=lambda: press("^")).grid(row=2, column=5, padx=10, pady=5)
Button(root, text="          C          ", command=clear).grid(row=1, column=6, padx=10, pady=5)
Button(root, text="          <-         ", command=back).grid(row=2, column=6, padx=10, pady=5)
Button(root, text="          =          ", command=calculate).grid(row=5, column=6, padx=10, pady=5)
Button(root, text="          (          ", command=lambda: press("(")).grid(row=3, column=6, padx=10, pady=5)
Button(root, text="          )          ", command=lambda: press(")")).grid(row=4, column=6, padx=10, pady=5)


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
