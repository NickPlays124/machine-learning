import tkinter as tk
import random

root = tk.Tk()
root.title("Game Tangkap Objek")
root.geometry("700x500")
root.config(bg="lightblue")

score = 0

judul = tk.Label(
    root, text="Game Tangkap Objek", 
    font=("Arial", 20, "bold"), bg="lightblue"
)
judul.pack(pady=10)

label_skor = tk.Label(root, text="Skor : 0", 
    font=("Arial", 14), bg="lightblue")
label_skor.pack()

canvas = tk.Canvas(root, width=600, height=350, bg="white")
canvas.pack(pady=20)

player = canvas.create_rectangle(50, 150, 100, 200, fill="blue")

target = canvas.create_oval(400, 150, 450, 200, fill="red")


def gerak(event):
    if event.keysym == "Left":
        canvas.move(player, -20, 0)
    elif event.keysym == "Right":
        canvas.move(player, 20, 0)
    elif event.keysym == "Up":
        canvas.move(player, 0, -20)
    elif event.keysym == "Down":
        canvas.move(player, 0, 20)

    cek_tabrakan()


def cek_tabrakan():
    global score
    player_pos = canvas.coords(player)
    target_pos = canvas.coords(target)

    if (
        player_pos[2] > target_pos[0]
        and player_pos[0] < target_pos[2]
        and player_pos[3] > target_pos[1]
        and player_pos[1] < target_pos[3]
    ):
        score += 1

        label_skor.config(text=f"Skor: {score}")

        x = random.randint(5, 500)
        y = random.randint(50, 250)

        canvas.coords(target, x, y, x + 50, y + 50)


root.bind("<Key>", gerak)

info = tk.Label(
    root,
    text="Gunakan tombol panah untuk menangkap target merah",
    font=("Arail", 13),
    bg="lightblue",
)
info.pack()

root.mainloop()