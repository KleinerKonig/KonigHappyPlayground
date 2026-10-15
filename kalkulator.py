
"""
Kalkulator Sederhana Python
Bisa melakukan operasi: penjumlahan (+), pengurangan (-), perkalian (x/*), dan pembagian (/)
"""

def penjumlahan(x, y):
    """Fungsi untuk penjumlahan dua angka"""
    return x + y

def pengurangan(x, y):
    """Fungsi untuk pengurangan dua angka"""
    return x - y

def perkalian(x, y):
    """Fungsi untuk perkalian dua angka"""
    return x * y

def pembagian(x, y):
    """Fungsi untuk pembagian dua angka"""
    if y == 0:
        return "Error! Pembagian dengan nol tidak diperbolehkan."
    return x / y

def kalkulator():
    """Fungsi utama kalkulator"""
    print("=== KALKULATOR BASIC ===")
    print("Pilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (x)")
    print("4. Pembagian (/)")
    print("5. Keluar")
    
    while True:
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ")
        
        if pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        
        if pilihan in ('1', '2', '3', '4'):
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid! Harap masukkan angka.")
                continue
            
            if pilihan == '1':
                result = penjumlahan(angka1, angka2)
                print(f"{angka1} + {angka2} = {result}")
            
            elif pilihan == '2':
                result = pengurangan(angka1, angka2)
                print(f"{angka1} - {angka2} = {result}")
            
            elif pilihan == '3':
                result = perkalian(angka1, angka2)
                print(f"{angka1} x {angka2} = {result}")
            
            elif pilihan == '4':
                result = pembagian(angka1, angka2)
                print(f"{angka1} : {angka2} = {result}")
        else:
            print("Pilihan tidak valid! Silakan pilih 1, 2, 3, 4, atau 5.")

if __name__ == "__main__":
    kalkulator()