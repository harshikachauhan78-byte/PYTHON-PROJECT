import tkinter as tk
import random

# Love-themed emojis
symbols = ["❤️", "💖", "💘", "💝", "💕", "🌹", "😘", "😍"]
cards = symbols * 2
random.shuffle(cards)

first_card = None
first_index = None
lock = False
matched = 0

buttons = []

def click(index):
    global first_card, first_index, lock, matched

    if lock:
        return

    btn = buttons[index]

    if btn["text"] != "":
        return

    btn.config(text=cards[index], state="disabled")

    if first_card is None:
        first_card = cards[index]
        first_index = index
    else:
        if first_card == cards[index]:
            matched += 2
            first_card = None
            first_index = None

            if matched == len(cards):
                result.config(text="❤️ You Matched All Love Cards! ❤️")
        else:
            lock = True

            def hide():
                global first_card, first_index, lock
                buttons[first_index].config(text="", state="normal")
                buttons[index].config(text="", state="normal")
                first_card = None
                first_index = None
                lock = False

            root.after(800, hide)

root = tk.Tk()
root.title("Love Letter Matching Game")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

for i in range(16):
    btn = tk.Button(
        frame,
        text="",
        width=6,
        height=3,
        font=("Arial", 18),
        command=lambda i=i: click(i)
    )
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)

result = tk.Label(root, text="", font=("Arial", 16), fg="red")
result.pack(pady=10)

root.mainloop()