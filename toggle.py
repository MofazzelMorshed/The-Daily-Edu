import tkinter as tk
is_up = True

def toggle():
    global is_up
    if is_up:
        btn.config(text="⬇ Down")
    else:
        btn.config(text="⬆ Up")
    is_up = not is_up

root = tk.Tk()
root.title("Toggle Up/Down")

btn = tk.Button(root, text="⬆ Up", font=("Helvetica", 20), width=10, command=toggle)
btn.pack(pady=20)


root.mainloop()
