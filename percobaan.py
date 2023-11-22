import tkinter as tk

def Hasil_Prediksi():
    nilai_fisika = int(entry1.get())
    nilai_kimia = int(entry2.get())
    nilai_ekonomi = int(entry3.get())

    nilai_tertinggi = max(nilai_fisika, nilai_kimia, nilai_ekonomi)
    
    if nilai_tertinggi >= 75:
        if nilai_tertinggi == nilai_fisika:
            hasil = "Elektro"
        elif nilai_tertinggi == nilai_kimia:
            hasil = "Kedokteran"
        elif nilai_tertinggi == nilai_ekonomi:
            hasil = "Management"
    else:
        hasil = "Tidak ada prediksi prodi berdasarkan nilai yang dimasukkan"
    
    Label_Prediksi.config(text=f"Hasil Prediksi Prodi: {hasil}")
    Label_Prediksi.grid(row=12, column=0, padx=10, pady=10)
    

Prediksi_Prodi_Pilihan = tk.Tk()
Prediksi_Prodi_Pilihan.geometry("500x400")

# create frame
frame = tk.Frame(Prediksi_Prodi_Pilihan)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# create entry (textbox)
entry1 = tk.Entry(frame)
entry2 = tk.Entry(frame)
entry3 = tk.Entry(frame)

# create label
Prediksi_Prodi_Label = tk.Label(frame, text="Aplikasi Prediksi Prodi Pilihan")
Label_Prediksi = tk.Label(frame)

button = tk.Button(frame, text="Hasil Prediksi", command=Hasil_Prediksi)

Prediksi_Prodi_Label.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=2, column=0, padx=10, pady=10)
entry3.grid(row=3, column=0, padx=10, pady=10)

button.grid(row=11, column=0, padx=10, pady=10)

Prediksi_Prodi_Pilihan.mainloop()