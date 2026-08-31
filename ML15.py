import tkinter as tk
import random

root = tk.Tk()
root.title("Game cepat tangkap ai")
root.geometry("700x500")
root.config(bg="lightblue")

score = 0
waktu = 30
game_aktif = True

judul = tk.Label(
    root, text="Game cepat tangkap ai", 
    font=("Arial", 20, "bold"), bg="lightblue"
)
judul.pack(pady=10)

label_skor = tk.Label(
    root, text="Skor: 0", font=("Arial", 14), bg="lightblue")
label_skor.pack()

label_waktu = tk.Label(
    root, text="Waktu: 30", font=("Arial", 14), bg="lightblue")
label_waktu.pack()

canvas = tk.Canvas(
    root, width=600, height=300, bg="white")
canvas.pack(pady=20)

target = canvas.create_oval(50, 50, 100, 100, fill="red")


def pindah_target():
    if not game_aktif:
        return

    x = random.randint(50, 500)
    y = random.randint(50, 200)

    canvas.coords(target, x, y, x + 50, y + 50)

    root.after(700, pindah_target)

def klik_target(event):
    global score
    if not game_aktif:
        return
    score += 1

    label_skor.config(text=f"Skor: {score}")

canvas.tag_bind(
    target, "<Button-1>", klik_target
)

def update_waktu():
    global waktu
    global game_aktif

    if waktu > 0:
        waktu -= 1

        label_waktu.config(text=f"Waktu: {waktu}")

        root.after(1000, update_waktu)

    else:
        game_aktif = False
        label_waktu.config(text="Waktu Habis")
        hasil.config(text=f"Skor Akhir {score}")


hasil = tk.Label(
    root, text="", 
    font=("Arial", 18, "bold"), 
    bg="lightblue")
hasil.pack(pady=10)

pindah_target()
update_waktu()

root.mainloop()