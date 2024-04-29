import json  # Mengimpor modul json untuk membaca file JSON.

def hitung_ipk(transkrip):
    total_sks = 0  # Inisialisasi total sks menjadi 0.
    total_bobot = 0  # Inisialisasi total bobot menjadi 0.
    
    # Iterasi melalui setiap mata kuliah dalam transkrip.
    for mata_kuliah in transkrip['mata_kuliah']:
        sks = mata_kuliah['sks']  # Mengambil jumlah SKS mata kuliah.
        nilai = mata_kuliah['nilai']  # Mengambil nilai mata kuliah.
        bobot = 0  # Inisialisasi bobot menjadi 0.
        
        # Menentukan bobot berdasarkan nilai.
        if nilai == 'A':
            bobot = 4.0
        elif nilai == 'A-':
            bobot = 3.7
        elif nilai == 'B+':
            bobot = 3.3
        elif nilai == 'B':
            bobot = 3.0
        elif nilai == 'B-':
            bobot = 2.7
        elif nilai == 'C+':
            bobot = 2.3
        elif nilai == 'C':
            bobot = 2.0
        elif nilai == 'C-':
            bobot = 1.7
        elif nilai == 'D+':
            bobot = 1.3
        elif nilai == 'D':
            bobot = 1.0
        elif nilai == 'E':
            bobot = 0.0
        
        total_sks += sks  # Menambahkan jumlah SKS ke total SKS.
        total_bobot += sks * bobot  # Menambahkan bobot SKS ke total bobot.
    
    # Menghitung dan mengembalikan IPK.
    if total_sks == 0:
        return 0.0
    else:
        return total_bobot / total_sks

# Mengambil transkrip dari file JSON.
with open('transkrip.json') as file:
    transkrip = json.load(file)

# Menghitung IPK dan mencetak hasilnya.
ipk = hitung_ipk(transkrip)
print("IPK:", ipk)
