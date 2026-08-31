import tkinter as tk
import random

root = tk.Tk()
root.title("AI Mengejar Target")
root.geometry("700x500")
root.config(bg="lightblue")

judul = tk.Label(
    root, text=" AI Mengejar Target", 
    font=("Arial", 20, "bold"), bg="lightblue"
)
judul.pack(pady=10)

canvas = tk.Canvas(root, width=600, height=350, bg="white")

canvas.pack()

ai = canvas.create_oval(50, 50, 100, 100, fill="blue")

target = canvas.create_oval(400, 200, 450, 250, fill="red")

def pindah_target(event):
    x = random.randint(50, 500)
    y = random.randint(50, 250)

    canvas.coords(target, x, y, x + 50, y + 50)

def gerak_ai():

    ai_pos = canvas.coords(ai)

    target_pos = canvas.coords(target)
    if ai_pos[0] < target_pos[0]:
        canvas.move(ai, 3, 0)
    elif ai_pos[0] > target_pos[0]:
        canvas.move(ai, -3, 0)
    if ai_pos[1] < target_pos[1]:
        canvas.move(ai, 0, 3)
    elif ai_pos[1] > target_pos[1]:
        canvas.move(ai, 0, -3)

    root.after(30, gerak_ai)


canvas.tag_bind(target, "<Button-1>", pindah_target)

info = tk.Label(
    root,
    text="Klik target merah agar AI mengejarnya",
    font=("Arial", 14),
    bg="lightblue",
)
info.pack(pady=15)

gerak_ai()
root.mainloop()