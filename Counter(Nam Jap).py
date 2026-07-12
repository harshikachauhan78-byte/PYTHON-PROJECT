from tkinter import *

root = Tk()
root.title("Counter App")
root.geometry("250x200")

count = 0

label = Label(root, text=str(count), font=("Arial", 30))
label.pack(pady=20)

def increase():
    global count
    count += 1
    label.config(text=str(count))

def decrease():
    global count
    count -= 1
    label.config(text=str(count))

Button(root, text="+", command=increase, width=10).pack(pady=5)
Button(root, text="-", command=decrease, width=10).pack(pady=5)

root.mainloop()