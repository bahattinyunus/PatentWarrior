# ⚙️ DOMINION_TECHNICAL: Ar-Ge & Tasarım

**"Önce yapıldığını kanıtlayabiliyorsan, monopolleri toza çevirebilirsin."**

Bu Dominion, patent savunmasının teknik cephesidir: **Önceki Teknik Analizi (Prior Art Analysis)** ve **Etrafından Dolaşma (Design Around)** stratejileri burada işlenir.

---

## 🛡️ Önceki Teknik Analizi (The "Invalidity" Attack)
Hedef, patentin başvuru tarihinden ("Priority Date") önce halka açıklanmış bir bilgi bularak, patentin "YENİ" olmadığını kanıtlamaktır.

### 1. Zaman Çizelgesi (The Timeline)
*   **Rüçhan Tarihi (Priority Date):** En kritik tarih. Bu tarihten 1 gün önce yayınlanmış bir bilgi bile patenti öldürür.
*   **Hoşgörü Süresi (Grace Period):** ABD'de mucidin kendi ifşaları için 1 yıllık süresi vardır. Ancak Avrupa ve Çin'de **YOKTUR**. (Mutlak Yenilik).

### 2. Ne "Prior Art" Sayılır?
*   **Eski Patentler:** En kolayıdır.
*   **Akademik Makaleler:** IEEE, ACM vb.
*   **KİTLE FONLAMASI (Crowdfunding):** Kickstarter veya Indiegogo projeleri ALTIN değerindedir. Buluşun yıllar önce çalıştığını videolu kanıtlarlar.
*   **YouTube:** Bir hobicinin garajında 2012'de çektiği video, 2015 tarihli bir patenti iptal ettirebilir.
*   **GitHub:** Açık kaynak kod commit tarihleri (`git log`), tartışılmaz kanıtlardır.

---

## 🔧 Etrafından Dolaşma (Design Around)
Eğer patent geçerliyse ve iptal ettiremiyorsanız, ürününüzü patentin kapsamına girmeyecek şekilde yeniden tasarlamalısınız.

### Strateji: "Element Eksiltme"
Bir patent istemi (Claim) bir yemek tarifi gibidir. Eğer tarifte "Un, Su ve Tuz" varsa ve siz sadece "Un ve Su" kullanırsanız, o tarifi (patenti) ihlal etmezsiniz.

1.  **Analiz:** Patentin 1. İstemini `templates/CLAIM_CHART_TEMPLATE.md` dosyasına yatırın.
2.  **Hedef Seçimi:** İstemdeki en gereksiz veya değiştirilebilir unsuru seçin.
3.  **Mühendislik:** O unsuru ürününüzden tamamen çıkarın veya başka bir yöntemle değiştirin.

**Örnek:**
*   **Patent İstemi:** "Veriyi (A) şifreleyen ve (B) Bluetooth ile gönderen cihaz."
*   **Sizin Ürününüz:** "Veriyi (A) şifreleyen ve (B) **Wi-Fi** ile gönderen cihaz."
*   **Sonuç:** Bluetooth elementini çıkardığınız için İHLAL YOKTUR.
