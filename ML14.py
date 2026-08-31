import tkinter as tk
from tkinter import ttk

BOBOT_LUCU = 0.4
BOBOT_MUDAH = 0.3
BOBOT_MURAH = 0.3

data_hewan = {
    "Kucing": {"lucu": 90, "mudah": 70, "murah": 60},
    "Ikan": {"lucu": 60, "mudah": 90, "murah": 85},
    "Hamster": {"lucu": 85, "mudah": 75, "murah": 80},
    "Kelinci": {"lucu": 95, "mudah": 60, "murah": 65},
}


def hitung_skor(nilai):
    return (
        nilai["lucu"] * BOBOT_LUCU
        + nilai["mudah"] * BOBOT_MUDAH
        + nilai["murah"] * BOBOT_MURAH
    )


def pilih_hewan_terbaik():
    hasil_text.delete("1.0", tk.END)

    skor_terbaik = -1
    hewan_terbaik = ""

    for nama, nilai in data_hewan.items():  # nama = kucing, nilai ={lucu mudah}
        skor = hitung_skor(nilai)

        hasil_text.insert(tk.END, f"{nama}\n")

        hasil_text.insert(
            tk.END,
            f"Lucu: {nilai['lucu']} | Mudah: {nilai['mudah']} | Murah: {nilai['murah']}\n",
        )
        hasil_text.insert(tk.END, f"Skor ai: {round(skor, 1)}\n\n")

        if skor > skor_terbaik:
            skor_terbaik = skor
            hewan_terbaik = nama

    label_pemenang.config(
        text=f"AI memilih {hewan_terbaik}\n Skor: {round(skor_terbaik, 1)}"
    )
    progress_pemenang["value"] = skor_terbaik


def lihat_detail(nama):
    nilai = data_hewan[nama]
    skor = hitung_skor(nilai)

    label_detail.config(
        text=(
            f"{nama}\n\n"
            f"Lucu: {nilai['lucu']}\n"
            f"Mudah dirawat: {nilai['mudah']}\n"
            f"Murah: {nilai['murah']}\n"
            f"Skor Total: {round(skor, 1)}"
        )
    )

    progress_detail["value"] = skor


root = tk.Tk()
root.title("AI Pilih hewan peliharaan")
root.geometry("650x600")
root.config(bg="#FFF4C2")

judul = tk.Label(
    root,
    text="Ai Pilih hewan pemeliharaan terbaik",
    font=("Arial", 20, "bold"),
    bg="#FFF4C2",
)
judul.pack(pady=15)

subjudul = tk.Label(
    root,
    text="Ai memilih berdasarkan bobot: Lucu 40%, Mudah dirawat 30%, Murah 30%",
    font=("Arial", 11),
    bg="#FFF4C2",
)
subjudul.pack()

frame_tombol = tk.Frame(root, bg="#FFF4C2")
frame_tombol.pack(pady=15)

for i, nama in enumerate(data_hewan.keys()):
    tombol = tk.Button(
        frame_tombol,
        text=nama,
        width=15,
        height=2,
        font=("Arial", 12, "bold"),
        command=lambda n=nama: lihat_detail(n),
    )
    tombol.grid(row=i // 2, column=1 % 2, padx=10, pady=10)

label_detail = tk.Label(
    root,
    text="Klik salah satu hewan untuk melihat nilainya",
    font=("Arial", 13),
    bg="#FFF4C2",
)
label_detail.pack(pady=10)

progress_detail = ttk.Progressbar(
    root, length=300, maximum=100)
progress_detail.pack(pady=5)

btn_ai = tk.Button(
    root, text="Jalankan AI", font=("Arial", 14, "bold"), 
    command=pilih_hewan_terbaik
)
btn_ai.pack(pady=15)

label_pemenang = tk.Label(
    root, text="", font=("Arial", 16, "bold"), bg="#FFF4C2")
label_pemenang.pack(pady=10)

progress_pemenang = ttk.Progressbar(
    root, length=350, maximum=100)
progress_pemenang.pack(pady=5)

hasil_text = tk.Text(
    root, width=65, height=10, font=("Arial", 10))
hasil_text.pack(pady=15)

root.mainloop()