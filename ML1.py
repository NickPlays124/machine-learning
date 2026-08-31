import turtle
import random

screen = turtle.Screen()
screen.title("Game Tebak Gambar AI Sederhana")
screen.bgcolor("lightblue")

pen = turtle.Turtle()
pen.pensize(5)
pen.speed(3)

def gambar_lingkaran():
    pen.clear()
    pen.circle(80)

def gambar_kotak():
    pen.clear()
    for i in range(4):
        pen.forward(150)
        pen.left(90)

def gambar_segitiga():
    pen.clear()
    for i in range(3):
        pen.forward(150)
        pen.left(120)

gambar = ["lingkaran", "kotak", "segitiga"]
pilihan = random.choice(gambar)



if pilihan == "lingkaran":
    gambar_lingkaran()

elif pilihan == "kotak":
    gambar_kotak()

elif pilihan == "segitiga":
    gambar_segitiga()

jawaban = screen.textinput("Tebak Gambar", "Ini gambar apa?")

if jawaban == pilihan:
    print("Benar! Kamu pintar!")
else:
    print("Salah, jawabannya adalah", pilihan)

turtle.done()