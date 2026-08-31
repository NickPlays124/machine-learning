import turtle

screen = turtle.Screen()
screen.title("Tebak Hewan atau Buah")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = {
    "kucing": "hewan",
    "ayam": "hewan",
    "sapi": "hewan",
    "apel": "buah",
    "pisang": "buah",
    "mangga": "buah",
    "jeruk": "buah",
    "anjing": "hewan",
    "semangka": "buah",
}

jawaban = screen.textinput("Tebak Data", "Masukan nama benda:")

if jawaban in data:
    hasil = data[jawaban]
    pen.goto(0, 0)
    pen.write(jawaban + " adalah " + hasil, align="center", font=("Arial", 20, "bold"))
else:
    pen.goto(0, 0)
    pen.write("Data tidak ditemukan", align="center", font=("Arial", 20, "bold"))

turtle.done()