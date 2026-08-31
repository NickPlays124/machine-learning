import tkinter as tk

root = tk.Tk()
root.title("Game Kontrol Ai")
root.geometry("700x500")
root.config(bg="lightblue")

judul = tk.Label(
    root, text="Game Kontrol AI", 
    font=("Arial", 20, "bold"), bg="lightblue"
)
judul.pack(pady=10)

canvas = tk.Canvas(
    root, width=600, height=350, bg="white")
canvas.pack()

player = canvas.create_rectangle(280, 150, 330, 200, fill="blue")

info = tk.Label(
    root, text="Gunakan Tombol Pnah Keyboard", 
    font=("Arial", 14), bg="lightblue"
)
info.pack(pady=15)


def gerak(event):
    if event.keysym == "Left":
        canvas.move(player, -20, 0)
    elif event.keysym == "Right":
        canvas.move(player, 20, 0)
    elif event.keysym == "Up":
        canvas.move(player, 0, -20)
    elif event.keysym == "Down":
        canvas.move(player, 0, 20)


root.bind("<Key>", gerak)

root.mainloop()