import tkinter as tk
from collections import Counter

data_warna = []

def tambah_warna():
    warna = entry.get().lower()
    if warna != "":
        data_warna.append(warna)
        label_info.config(text=f"Data tersimpan: {len(data_warna)} warna")
        entry.delete(0, tk.END)


def tampilkan_hasil():
    if len(data_warna) == 0:
        label_hasil.config(text="Belum ada data!")
        return

    hitung = Counter(data_warna)
    favorit = hitung.most_common(1)[0][0]

    label_hasil.config(text=f"Warna Favorit: {favorit}")

    try:
        root.config(bg=favorit)

    except:
        root.config(bg="white")


root = tk.Tk()
root.title("AI Belajar warna favorit")
root.geometry("400x300")

# judul
label_title = tk.Label(root, text="AI Belajar warna", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# input
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# tomboltambah
btn_tambah = tk.Button(root, text="Tambah Warna", command=tambah_warna)
btn_tambah.pack(pady=5)

# infodata
label_info = tk.Label(root, text="Belum ada data", font=("Arial", 10))
label_info.pack(pady=5)

# tombolhasil
btn_hasil = tk.Button(root, text="Lihat Hasil", command=tampilkan_hasil)
btn_hasil.pack(pady=10)

# output
label_hasil = tk.Label(root, text="", font=("Arial", 14))
label_hasil.pack(pady=10)

root.mainloop()
