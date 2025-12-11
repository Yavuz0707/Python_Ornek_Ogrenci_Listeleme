class Ogrenci:
    def __init__(self, numara, ad, soyad, ortalama=None):
        self.numara = numara
        self.ad = ad
        self.soyad = soyad
        self.ortalama = ortalama

    def not_gir(self):
        while True:
            try:
                ort = float(input("Ortalama girin (0-100): "))
                if 0 <= ort <= 100:
                    self.ortalama = ort
                    print("Not başarıyla kaydedildi.")
                    break
                else:
                    print("Hata: Not 0 ile 100 arasında olmalıdır!")
            except ValueError:
                print("Hata: Lütfen sadece rakam girin!")

    def bilgileri_goster(self):
        return f"{self.numara} - {self.ad} - {self.soyad} - {self.ortalama if self.ortalama is not None else 'Henüz not girilmedi'}"


def menu_goster():
    print("\n Öğrenci Bilgi Sistemi")
    print("------------------------")
    print("1. Öğrenci Ekle")
    print("2. Öğrenci Sil")
    print("3. Öğrencileri Listele")
    print("4. Öğrenci Not Gir")
    print("5. Öğrenci Bilgilerini Göster")
    print("6. Okul Not Ortalaması")
    print("7. Çıkış")


def okul_ortalama_hesapla(ogrenciler):
    toplam = 0
    sayi = 0

    for ogr in ogrenciler.values():
        if ogr.ortalama is not None:
            toplam += ogr.ortalama
            sayi += 1

    if sayi > 0:
        print("Okul Genel Not Ortalaması:", toplam / sayi)
    else:
        print("Henüz hiçbir öğrenciye not girilmemiş.")


def main():
    ogrenciler = {}

    while True:
        menu_goster()
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            numara = input("Öğrenci numarası: ")
            ad = input("Ad: ")
            soyad = input("Soyad: ")

            if numara in ogrenciler:
                print("Bu numara zaten kayıtlı!")
            else:
                ogrenciler[numara] = Ogrenci(numara, ad, soyad)
                print("Öğrenci eklendi.")

        elif secim == "2":
            numara = input("Silinecek öğrenci numarası: ")
            if numara in ogrenciler:
                del ogrenciler[numara]
                print("Öğrenci silindi.")
            else:
                print("Bu numara bulunamadı.")

        elif secim == "3":
            if ogrenciler:
                print("\n--- Öğrenci Listesi ---")
                for ogr in ogrenciler.values():
                    print(ogr.bilgileri_goster())
            else:
                print("Kayıtlı öğrenci yok.")

        elif secim == "4":
            numara = input("Not girilecek öğrenci numarası: ")
            if numara in ogrenciler:
                ogrenciler[numara].not_gir()
            else:
                print("Öğrenci bulunamadı.")

        elif secim == "5":
            numara = input("Gösterilecek öğrenci numarası: ")
            if numara in ogrenciler:
                print(ogrenciler[numara].bilgileri_goster())
            else:
                print("Öğrenci bulunamadı.")

        elif secim == "6":
            okul_ortalama_hesapla(ogrenciler)

        elif secim == "7":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! (1–7)")


main()
