# Öğrenci Bilgi Sistemi (v1.0)

Bu proje, Python kullanılarak geliştirilmiş **konsol tabanlı** bir Öğrenci Bilgi Sistemi uygulamasıdır. Uygulama, öğrenci bilgilerini dosya tabanlı olarak saklar ve temel öğrenci yönetim işlemlerini gerçekleştirmeyi sağlar.

---

## 📌 Proje Özeti

Öğrenci Bilgi Sistemi; öğrenci ekleme, silme, not girme, öğrenci bilgilerini görüntüleme ve okul genel not ortalamasını hesaplama işlemlerini yapabilen basit ve anlaşılır bir uygulamadır. Girilen veriler `.txt` dosyasında saklanır ve program yeniden çalıştırıldığında otomatik olarak yüklenir..

---

## ⚙️ Özellikler

* Öğrenci ekleme
* Öğrenci silme
* Tüm öğrencileri listeleme
* Öğrenciye not girme (0–100 arası kontrol)
* Tek öğrenci bilgisi görüntüleme
* Okul genel not ortalaması hesaplama
* Dosyadan veri okuma ve dosyaya veri kaydetme
* Hatalı girişler için kullanıcı uyarıları

---

## 🗂️ Dosya Yapısı

```
Öğrenci Bilgi Sistemi v1.0/
│
├── veriler.txt          # Öğrenci verilerinin tutulduğu dosya
├── main.py              # Uygulamanın ana Python dosyası
```

---

## 🧱 Kullanılan Yapılar

* **Sınıf (Class):** `Ogrenci`
* **Dosya İşlemleri:** `open`, `readlines`, `write`
* **Veri Yapısı:** Dictionary (öğrenciler numaraya göre tutulur)
* **Hata Kontrolü:** `try-except`, koşul kontrolleri

---

## ▶️ Uygulamanın Çalıştırılması

1. Bilgisayarınızda Python 3 yüklü olmalıdır.
2. Proje klasörüne girin.
3. Terminal veya komut satırında aşağıdaki komutu çalıştırın:

```bash
python main.py
```

---

## 📋 Menü Seçenekleri

```
1. Öğrenci Ekle
2. Öğrenci Sil
3. Öğrencileri Listele
4. Öğrenci Not Gir
5. Öğrenci Bilgilerini Göster
6. Okul Not Ortalaması
7. Çıkış
```

---

## 🛡️ Hata Kontrolleri

* Aynı öğrenci numarası ile kayıt yapılamaz
* Not girişi sadece sayısal ve 0–100 arası kabul edilir
* Kayıtlı olmayan öğrenci için işlem yapılamaz
* Dosya yoksa program hata vermeden çalışır

---

## 🧪 Geliştirme Amacı

Bu proje, Python'da:

* sınıf yapısını
* dosya işlemlerini
* fonksiyon kullanımını
* kullanıcıdan veri almayı
* hata kontrol mekanizmalarını
  öğrenmek ve pekiştirmek amacıyla geliştirilmiştir.

---

## 📎 Not

Bu proje eğitim amaçlıdır ve geliştirilmeye açıktır. İlerleyen sürümlerde dosya formatı, arayüz veya veritabanı desteği eklenebilir.
