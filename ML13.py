import tkinter as tk
from collections import Counter

data_aktivitas = []


def tambah_aktivitas():
    aktivitas = entry.get().lower()
    if aktivitas != "":
        data_aktivitas.append(aktivitas)

        label_info.config(text=f"Data tersimpan: {len(data_aktivitas)}")

        entry.delete(0, tk.END)


def rekomendasi_ai():
    if len(data_aktivitas) == 0:
        label_hasil.config(text="Belum ada data")
        return
    hitung = Counter(data_aktivitas)

    hasil = hitung.most_common(1)[0][0]

    label_hasil.config(text=f"AI merekomendasikan: {hasil}")


root = tk.Tk()
root.title("AI Probability Activity")
root.geometry("450x350")

judul = tk.Label(
    root, 
    text="AI Rekomendasi aktivitas", font=("Arial", 16, "bold"))

judul.pack(pady=10)

entry = tk.Entry(
    root, font=("Arial", 12))

entry.pack(pady=5)

btn_tambah = tk.Button(
    root, text="Tambah Aktivitas", command=tambah_aktivitas)

btn_tambah.pack(pady=5)

label_info = tk.Label(
    root, text="Belum ada data")

label_info.pack()

btn_rekomendasi = tk.Button(
    root, text="Lihat Rekomendasi", command=rekomendasi_ai)

btn_rekomendasi.pack(pady=10)

label_hasil = tk.Label(
    root, text="", font=("Arial", 14), wraplength=300)

label_hasil.pack(pady=20)

root.mainloop()