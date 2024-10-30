class PersegiPanjang:
    def __init__(self, panjang, lebar): #init(konstruktor)
        self.panjang = panjang
        self.lebar = lebar

    def keliling(self): # self  menyimpan nilai panjang dan lebar ke dalam objek.
        return 2 * (self.panjang + self.lebar)#mengembalikan nilai

    def luas(self):
        return self.panjang * self.lebar

    def __str__(self):
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

def main():
    try:
        # Meminta input dari pengguna untuk panjang dan lebar
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))

        # Membuat objek persegi panjang dengan panjang dan lebar yang diberikan
        persegi_panjang = PersegiPanjang(panjang, lebar)

        # Menampilkan hasil
        print(persegi_panjang)  # Memanggil fungsi __str__
        print("Keliling:", persegi_panjang.keliling(), "cm")
        print("Luas:", persegi_panjang.luas(), "cm^2")
    
    except ValueError:
        print("Input tidak valid! Harap masukkan angka untuk panjang dan lebar.")

# Memanggil fungsi main
if __name__ == "__main__":
    main()

