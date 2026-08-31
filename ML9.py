import turtle
import random

screen = turtle.Screen()
screen.title("Game Skor Ai")
screen.bgcolor("lightyellow")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = ["apel", "pisang", "apel", "pisang", "apel"]

score = 0

def ai_tebak():
    return random.choice(["apel", "pisang"])

y_pos = 100

for i in range(len(data)):

    label_asli = data[i]
    prediksi = ai_tebak()

    if prediksi == label_asli:
        hasil = "Benar"
        score += 10
    else:
        hasil = "Salah"

    pen.goto(-200, y_pos)
    pen.write(f"Asli: {label_asli}", font=("Arial", 12, "normal"))

    pen.goto(0, y_pos)
    pen.write(f"Ai: {prediksi}", font=("Arial", 12, "normal"))

    pen.goto(150, y_pos)
    pen.write(hasil, font=("Arial", 12, "bold"))

    y_pos -= 40

pen.goto(-50, -150)
pen.write(f"Skor Akhir: {score}", font=("Arial", 16, "bold"))

turtle.done()