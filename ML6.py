import turtle
import random

screen = turtle.Screen()
screen.title("Game Keputusan AI")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

cuaca = ["hujan", "cerah"]

kondisi = random.choice(cuaca)

pertanyaan = "kalau " + kondisi + " maka apa?"
pen.goto(0, 50)
pen.write(pertanyaan, align="center", font=("Arial", 20, "normal"))

jawaban = screen.textinput("Jawaban", "Apa yang harus dilakukan?")

if kondisi == "hujan" and jawaban == "pakai payung":
    hasil = "Benar! Kamu siap menghadapi hujan."
elif kondisi == "cerah" and jawaban == "bermain":
    hasil = "Benar! Kamu bisa bermain diluar"
else:
    hasil = " Belum tepat, coba lagi!"

pen.goto(0, -50)
pen.write(hasil, align="center", font=("Arial", 20, "normal"))

turtle.done()
