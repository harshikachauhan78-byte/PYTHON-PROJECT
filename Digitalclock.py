import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.configure(bg="black")

# Function to update time
def update_time():
    current_time = strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

# Clock label
label = tk.Label(
    root,
    font=("Arial", 50, "bold"),
    background="black",
    foreground="lime"
)
label.pack(anchor="center")

update_time()

# Run application
root.mainloop()