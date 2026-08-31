import turtle
import random

screen = turtle.Screen()
screen.title("Game Tebak Emoji")


pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = {"🫩": "wajah", 
        "🦝": "hewan", 
        "🥝": "buah", 
        "🚙": "kendaraan"
    }


emoji = random.choice(list(data.keys()))

pen.goto(0, 30)
pen.write(emoji, align="center", font=("Arial", 80, "normal"))

jawaban = screen.textinput("Tebak emoji", "Emoji ini termasuk kategori apa?")

if jawaban.lower() == data[emoji]:
    print("Benar! kamu hebat")
else:
    print("Belum tepat")
    print("Jawaban yang benar:", data[emoji])

turtle.done()
