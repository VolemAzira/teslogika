def cari_kata(teks):
    kata_kunci = ["sang gajah", "serigala", "harimau"]
    hasil = []

    for kata in kata_kunci:
        indeks = teks.find(kata)
        while indeks != -1:
            hasil.append(kata)
            indeks = teks.find(kata, indeks + 1)

    return " - ".join(hasil)

# Contoh penggunaan
print ("Volem Alvaro Azira")
teks_masukan = "Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah."
hasil_pencarian = cari_kata(teks_masukan)
print(hasil_pencarian)
