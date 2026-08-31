import turtle
import random

screen = turtle.Screen()
screen.title("AI pilih makanan")
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data_makanan = {
    "apel": "sehat",
    "pisang": "sehat",
    "permen": "manis",
    "donat": "manis",
    "nasi goreng": "berat",
    "mie": "berat",
    "seblak": "pedas",
    "makaroni": "pedas",
}


def tampilkan_hasil(kategori):
    rekomendasi = []
    for makanan, kat in data_makanan.items():
        if kat == kategori:
            rekomendasi.append(makanan)

        pen.clear()

    if rekomendasi:
        hasil = random.choice(rekomendasi)
        pesan = "AI memilih " + hasil
    else:
        pesan = "Pilihan tidak ada"

    pen.goto(0, -50)
    pen.write(pesan, align="center", font=("Arial", 20, "bold"))


def klik(x, y):
    if -150 < x < -50 and 0 < y < 50:
        tampilkan_hasil("sehat")

    elif -50 < x < 50 and 0 < y < 50:
        tampilkan_hasil("manis")

    elif 50 < x < 150 and 0 < y < 50:
        tampilkan_hasil("berat")

def buat_tombol(x, y, text):
    pen.goto(x, y)
    pen.pendown()

    for _ in range(2):
        pen.forward(100)
        pen.left(90)
        pen.forward(50)
        pen.left(90)

    pen.penup()
    pen.goto(x + 50, y + 10)
    pen.write(text, align="center", font=("Arial", 12, "bold"))


pen.goto(0, 100)
pen.write("Pilih jenis makanan", align="center", font=("Arial", 24, "bold"))

buat_tombol(-150, 0, "Sehat")
buat_tombol(-50, 0, "Manis")
buat_tombol(50, 0, "Berat")

screen.onclick(klik)

turtle.done()