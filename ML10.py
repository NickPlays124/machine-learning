import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.title("AI Rekomendasi Aktivitas")

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

bot = turtle.Turtle()
bot.shape("circle")
bot.shapesize(3)
bot.penup()
bot.speed(1)

waktu = screen.textinput(
    "Input Waktu", "Masukan Waktu:\npagi / siang / sore / malam"
)

if waktu == "pagi":
    bg = "lightyellow"
    aktivitas = "Olahraga Pagi"
    emoji = "☀️"
    posisi = (-200, 0)
elif waktu == "siang":
    bg = "skyblue"
    aktivitas = "Belajar dan membaca"
    emoji = "📖"
    posisi = (0, 0)
elif waktu == "sore":
    bg = "orange"
    aktivitas = "Bermain di luar"
    emoji = "⚽"
    posisi = (200, 0)
elif waktu == "malam":
    bg = "darkblue"
    aktivitas = "Istirahat dan tidur"
    emoji = "🌙"
    posisi = (0, -100)
else:
    bg = "gray"
    aktivitas = "Waktu tidak dikenali"
    emoji = "❓"
    posisi = (0, 0)

screen.bgcolor(bg)

bot.goto(posisi)

pen.goto(0, 220)
pen.write(
    "RULE-BASED AI", 
    align="center", 
    font=("Arial", 24, "bold"))

pen.goto(0, 150)
pen.write(
    f"{emoji} Rekomendasi Aktivitas:", 
    align="center", 
    font=("Arial", 20, "bold")
)

pen.goto(0, 100)
pen.write(aktivitas, 
          align="center", 
          font=("Arial", 22, "normal"))

pen.goto(0, -250)
pen.write(
    "AI memilih berdasarkan aturan waktu", 
    align="center", 
    font=("Arial", 14, "italic")
)

turtle.done()
