import turtle
import random

screen = turtle.Screen()
screen.title("Game Tebak Pola")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

pola = {"1, 2, 3, ?": "4", 
        "2, 4, 6, ?": "8", 
        "merah, biru, merah, ?": "biru"
}

soal = random.choice(list(pola.keys()))

pen.goto(0, 50)
pen.write("Tebak pola berikut:", align="center", font=("Arial", 20, "normal"))

pen.goto(0, 0)
pen.write(soal, align="center", font=("Arial", 24, "normal"))

jawaban = screen.textinput("Jawaban", "Angka atau kata berikutnya adalah?")

if jawaban == pola[soal]:
    hasil = "Benar! kamu berhasil mengenali polanya."
else:
    hasil = "belum tepat. jawaban yang benar adalah" + pola[soal]

pen.goto(0, -50)
pen.write(hasil, align="center", font=("Arial", 18, "normal"))

turtle.done()