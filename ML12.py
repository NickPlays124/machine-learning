import tkinter as tk
from collections import Counter

history = []

def tambah_data():
    pilihan = entry.get().lower()
    if pilihan != "":
        history.append(pilihan)
        label_info.config(text=f"Total data:{len(history)}")
        entry.delete(0, tk.END)


def rekomendasi_ai():
    if len(history) == 0:
        label_hasil.config(text="Belum ada data")
        return

    hitung = Counter(history)
    hasil = hitung.most_common(1)[0][0]

    label_hasil.config(text=f"Rekomendasi: {hasil}")


root = tk.Tk()
root.title("Memory AI")
root.geometry("400x300")

judul = tk.Label(root, text="AI Memory system", font=("Arial", 16, "bold"))
judul.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

btn_tambah = tk.Button(root, text="Tambah Data", command=tambah_data)
btn_tambah.pack(pady=5)

label_info = tk.Label(root, text="Belum ada data")
label_info.pack()

btn_hasil = tk.Button(root, text="Lihat Rekomendasi", command=rekomendasi_ai)
btn_hasil.pack(pady=10)

label_hasil = tk.Label(root, text="", font=("Arial", 14))
label_hasil.pack()

root.mainloop()
