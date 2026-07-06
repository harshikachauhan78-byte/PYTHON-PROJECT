import tkinter as tk
from tkinter import messagebox
import random
import time

# Sample paragraphs
paragraphs = [
    "Python is an easy and powerful programming language.",
    "Practice every day to improve your typing speed and accuracy.",
    "Artificial intelligence is transforming the future of technology.",
    "Learning to code requires patience, consistency, and curiosity."
]

start_time = 0

# Start timer
def start_typing(event):
    global start_time
    if start_time == 0:
        start_time = time.time()

# Check typing speed
def check_result():
    global start_time

    end_time = time.time()
    total_time = end_time - start_time

    original = text_label["text"]
    typed = input_box.get()

    # Count correct characters
    correct = 0
    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    accuracy = (correct / len(original)) * 100

    words = len(typed.split())
    wpm = (words / total_time) * 60

    messagebox.showinfo(
        "Result",
        f"Time: {total_time:.2f} sec\n"
        f"WPM: {wpm:.2f}\n"
        f"Accuracy: {accuracy:.2f}%"
    )

# Restart test
def restart():
    global start_time
    start_time = 0

    input_box.delete(0, tk.END)
    text_label.config(text=random.choice(paragraphs))

# GUI
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("700x350")

title = tk.Label(
    root,
    text="Typing Speed Test",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

text_label = tk.Label(
    root,
    text=random.choice(paragraphs),
    wraplength=650,
    font=("Arial", 14)
)
text_label.pack(pady=15)

input_box = tk.Entry(root, font=("Arial", 14), width=60)
input_box.pack(pady=10)
input_box.bind("<Key>", start_typing)

submit_btn = tk.Button(
    root,
    text="Check Result",
    command=check_result,
    font=("Arial", 12)
)
submit_btn.pack(pady=10)

restart_btn = tk.Button(
    root,
    text="Restart",
    command=restart,
    font=("Arial", 12)
)
restart_btn.pack()

root.mainloop()