import tkinter as tk

# Fungsi untuk menampilkan hasil
def tampilkan_hasil():
    nama = entry_nama.get()
    usia = entry_usia.get()
    jenis_kelamin = entry_jenis_kelamin.get()
    asal_sekolah = entry_asal_sekolah.get()
    
    # Cek apakah semua data terisi
    if not nama or not usia or not jenis_kelamin or not asal_sekolah:
        label_hasil.config(text = 'Semua data harus diisi!', fg='red')
        tampilkan(hal2)
   
    elif not usia.isdigit():
        label_hasil.config(text = 'Usia harus berupa angka!', fg='red')
        tampilkan(hal2)

    elif jenis_kelamin == 'L' or jenis_kelamin=='P':
        label_hasil.config(text=f"Registrasi berhasil!\nNama : {nama}\nUsia : {usia}\nJenis kelamin : {jenis_kelamin}\nAsal sekolah : {asal_sekolah}",fg="green")
        tampilkan(hal2)

    else:
        label_hasil.config(text = 'Jenis Kelamin harus L atau P!', fg='red')
        tampilkan(hal2)

def tampilkan(frame):
    frame.tkraise()

# Membuat jendela utama
jendela =tk.Tk()
jendela.title('Form Registrasi Siwa Baru')

hal1=tk.Frame(jendela)


# Label dan Entry Nama
label_judul1 = tk.Label(hal1, text="Nama Lengkap:")
label_judul1.pack()
entry_nama = tk.Entry(hal1)
entry_nama.pack()

# Label dan Entry Usia
label_judul2= tk.Label(hal1, text="Usia :")
label_judul2.pack()
entry_usia = tk.Entry(hal1)
entry_usia.pack()

# Label dan Entry Jenis Kelamin
label_judul3= tk.Label(hal1, text="Jenis Kelamin (L/P) :")
label_judul3.pack()
entry_jenis_kelamin = tk.Entry(hal1)
entry_jenis_kelamin.pack()

# Label dan Entry Asal Sekolah
label_judul4= tk.Label(hal1, text="Asal Sekolah :")
label_judul4.pack()
entry_asal_sekolah = tk.Entry(hal1)
entry_asal_sekolah.pack()

# Tombol untuk submit
tombol1 = tk.Button(hal1, text="Daftar", command= tampilkan_hasil)
tombol1.pack()

hal2=tk.Frame(jendela)
label_hasil = tk.Label(hal2, text="")
label_hasil.pack()


tombol2=tk.Button(hal2, text="Reset", command= lambda:tampilkan(hal1))
tombol2.pack()
tampilkan(hal1)

for frame in(hal1,hal2):
    frame.place(x=0,y=0,relwidth=1,relheight=1)

# Label untuk menampilkan hasil


# Menjalankan GUI
jendela.mainloop()

    