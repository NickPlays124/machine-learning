import turtle
import random

screen = turtle.Screen()
screen.title("Sorting Warna dan Bentuk")
screen.bgcolor("White")

pen = turtle.Turtle()
pen.pensize(5)
pen.speed(3)


warna = ["red", "blue", "green", "yellow"]

bentuk = ["lingkaran", "kotak", "segitiga"]


def gambar_lingkaran(warna):
    pen.clear()
    pen.color(warna)
    pen.begin_fill()
    pen.circle(60)
    pen.end_fill()


def gambar_kotak(warna):
    pen.clear()
    pen.color(warna)
    pen.begin_fill()
    for i in range(4):
        pen.forward(150)
        pen.left(90)
    pen.end_fill()


def gambar_segitiga(warna):
    pen.clear()
    pen.color(warna)
    pen.begin_fill()
    for i in range(3):
        pen.forward(120)
        pen.left(120)
    pen.end_fill()


pilih_warna = random.choice(warna)

pilih_bentuk = random.choice(bentuk)

if pilih_bentuk == "lingkaran":
    gambar_lingkaran(pilih_warna)
elif pilih_bentuk == "kotak":
    gambar_kotak(pilih_warna)
elif pilih_bentuk == "segitiga":
    gambar_segitiga(pilih_warna)

jawab_bentuk = screen.textinput("Tebak Bentuk", "Bentuk apa ini?")
jawab_warna = screen.textinput("Tebak Warna", "Warnanya apa?")

if jawab_bentuk == pilih_bentuk and jawab_warna == pilih_warna:
    print("Hebat jawaban kamu benar!")
else:
    print("Belum tepat")
    print("Bentuk:", pilih_bentuk)
    print("Warna:", pilih_warna)

turtle.done()
