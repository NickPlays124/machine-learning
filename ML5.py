import turtle
import random

screen = turtle.Screen()
screen.title("Tebak Angka Pintar")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

angka_rahasia = random.randint(1, 10)

tebakan = screen.textinput("Tebak Angka", "Masukan angka 1 sampai 10:")

tebakan = int(tebakan)

if tebakan == angka_rahasia:
    hasil = "Benar! Kamu hebat"
elif tebakan > angka_rahasia:
    hasil = "Terlalu besar"
else:
    hasil = "Terlalu kecil"

pen.goto(0, 0)
pen.write(hasil, align="center", font=("Arial", 50, "normal"))

turtle.done()