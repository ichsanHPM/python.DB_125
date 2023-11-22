import tkinter as tk
import sqlite3

#fungsi untuk membuat tabel jika belum ada
def create_table():
    connection = sqlite3.connect('basisdata.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai (
                        id INTEGER PRIMARY KEY,
                        nama_siswa TEXT,
                        nilai_biologi INTEGER,
                        nilai_fisika INTEGER,
                        nilai_inggris INTEGER,
                        prediksi INTEGER
                    )''')
    connection.commit()
    connection.close()

#fungsi untuk memasukan data ke dalam database
def insert_data():
    nama_siswa = entry_nama_siswa.get()
    nilai_biologi = int(entry_nilai_biologi.get())
    nilai_fisika = int(entry_nilai_fisika.get())
    nilai_inggris = int(entry_nilai_inggris.get())
    
    max_nilai = max(nilai_biologi, nilai_fisika, nilai_inggris)
    Hasil_Prediksi = " "
    if max_nilai == nilai_biologi:
        Hasil_Prediksi = "Kedokteran"
    elif max_nilai == nilai_fisika:
        Hasil_Prediksi = "Teknik"
    elif max_nilai == nilai_inggris:
        Hasil_Prediksi = "Bahasa"
        
    hasil.config(text=f"Hasil Prediksi : {Hasil_Prediksi}")

    connection = sqlite3.connect('basisdata.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO nilai (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, prediksi)
                       VALUES (?, ?, ?, ?, ?)''', (nama_siswa, nilai_biologi, nilai_fisika, nilai_inggris, Hasil_Prediksi))
    connection.commit()
    connection.close()

#Fungsi untuk menyimpan data setelah tombol "simpan" ditekan
def simpan_data():
    insert_data()
    entry_nama_siswa.delete(0, tk.END)
    entry_nilai_biologi.delete(0, tk.END)
    entry_nilai_fisika.delete(0, tk.END)
    entry_nilai_inggris.delete(0, tk.END)


#Membuat tabel jika belum ada
create_table()

#Membuat GUI menggunakan TKinter
root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama_siswa = tk.Label(root, text="Nama Siswa: ")
label_nama_siswa.pack()
entry_nama_siswa = tk.Entry(root)
entry_nama_siswa.pack()

label_nilai_biologi = tk.Label(root, text="Nilai Biologi: ")
label_nilai_biologi.pack()
entry_nilai_biologi = tk.Entry(root)
entry_nilai_biologi.pack()

label_nilai_fisika = tk.Label(root, text="Nilai Fisika: ")
label_nilai_fisika.pack()
entry_nilai_fisika = tk.Entry(root)
entry_nilai_fisika.pack()

label_nilai_inggris = tk.Label(root, text="Nilai Ingrris: ")
label_nilai_inggris.pack()
entry_nilai_inggris = tk.Entry(root)
entry_nilai_inggris.pack()

button_simpan = tk.Button(root, text="Simpan", command=simpan_data)
button_simpan.pack()

hasil = tk.Label(root, text="Hasil Prediksi : ")
hasil.pack()

root.mainloop()