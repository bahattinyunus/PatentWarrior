# 🔍 DOMINION_SEARCH: Radar & İstihbarat

**"Google yetersizdir. Makinenin diliyle konuşmalısınız."**

Patent araştırması, bir patenti hükümsüz kılacak veya sizin güvende olduğunuzu kanıtlayacak o "samanlıktaki iğneyi" bulma sanatıdır. Bu Dominion, istihbarat toplama ve hedef belirleme merkezidir.

---

## 🛠️ YENİ: Taktiksel Sorgu Üretici (Tactical Query Generator)
Karmaşık operatörleri ezberlemenize gerek kalmadan, ileri seviye arama dizileri üreten Python tabanlı bir araç geliştirdik.

### Kullanım (Usage)
1.  Ana dizine gidin (Terminal/Komut İstemi).
2.  Aşağıdaki komutu çalıştırın:
    ```bash
    python core/query_gen.py "anahtar_kelime" "diger_kelime" --assignee "RakipFirma"
    ```
3.  Araç size **Google Patents** ve **Espacenet** için hazır linkler üretecektir. Bu linkleri tarayıcınıza kopyalayın.

### Örnek Senaryo
Otonom araçlar için "Lidar" teknolojisini araştırıyorsunuz ve 2015 öncesi (eski teknik) bulgulara ihtiyacınız var:
```bash
python core/query_gen.py "lidar" "autonomous" --before "2015-01-01"
```
*Çıktı, size 2015 öncesi tarihli Lidar patentlerini listeleyen doğrudan bir istihbarat linki verecektir.*

---

## 🧠 Manuel Arama Stratejileri (Black Ops Search)

### 1. Kelime Genişletme (Keyword Expansion)
Mühendisler "Drone" der, Avukatlar "Unmanned aerial vehicle" der.
*   **Yanlış:** Sadece "Drone" aramak.
*   **Doğru:** "Unmanned aerial vehicle" OR "UAV" OR "Rotorcraft" OR "Aerial surveillance device"

### 2. Sınıflandırma Kodları (The Fingerprint)
Kelimeler yalan söyler, kodlar söylemez.
*   İlgili tek bir patent bulun.
*   Onun **CPC Koduna** bakın (örneğin: `G06F17/30`).
*   Sadece bu kodu tarayarak, o teknolojiye ait tüm "gizli" patentleri dökün.

### 3. "Assignee" Tuzağı
*   Büyük şirketler patentleri bazen paravan şirketler üzerine, bazen de doğrudan kurucu mühendislerin (Inventor) şahsi isimlerine kaydeder.
*   Rakibinizin "Yıldız Mühendislerini" LinkedIn'den bulun ve onların adıyla patent arayın.

---

## 🌍 Veritabanı Üsleri
*   **Google Patents**: Hızlı tarama, çeviri ve görselleştirme için.
*   **Espacenet**: Avrupa ve Asya (Çin/Japonya/Kore) verilerine erişim için kritik.
*   **WIPO Patentscope**: Uluslararası (PCT) başvurularının erken tespiti için.
