# Educational Dataset Converter

\[English version below]

---

## Proje Amacı

**Educational Dataset Converter**, Türkiye'deki eğitim materyallerini (`ders kitapları, çalışma kağıtları, müfredat içerikleri`) doğal dil işleme modellerinde kullanılabilir `"input", "output"` formatında veri setlerine dönüştürmeyi amaçlayan açık kaynak bir projedir.

Üretilen veriler [Hugging Face Datasets](https://huggingface.co/datasets/abdbali) üzerinde paylaşılarak öğretmen, araştırmacı, geliştirici ve içerik üreticilerine açık biçimde sunulmaktadır.

---

## Dizin Yapısı

```bash
educational-dataset-converter/
├── data/
│   └── mevsimler_iklim_veriseti.csv
├── scripts/
│   └── convert_to_csv.py
├── notebooks/
│   └── 01_csv_cevirici.ipynb
├── uploads_to_huggingface/
│   └── dataset_card_template.md
└── README.md
```

---

## Kurulum

```bash
pip install pandas datasets huggingface_hub
```

---

## Kullanım

### Python Script ile Dönüştürme

```bash
python scripts/convert_to_csv.py --input kitap_metni.txt --output data/mevsimler_iklim_veriseti.csv
```

Script, verilen metin dosyasındaki anlamlı soru-cevap çiftlerini çıkartarak `"input", "output"` formatında CSV dosyasına dönüştürür.

### Jupyter Notebook (Etki̇n Geli̇şti̇rme İçin)

```python
from scripts.convert_to_csv import convert_text_to_csv
convert_text_to_csv("kitap_metni.txt", "data/output.csv")
```

---

## Örnek Veri

```csv
"input","output"
"İklim nedir?","Yeryüzünün bir kısmında uzun yıllar boyunca gözlenen hava olaylarının ortalamasıdır."
"21 Mart’ta gece ve gündüz süreleri nasıldır?","Eşittir, 12 saat"
```

---

## Hugging Face Yükleme Rehberi

```bash
huggingface-cli login
huggingface-cli repo create abdbali/educational-dataset-converter

git clone https://huggingface.co/datasets/abdbali/educational-dataset-converter
cd educational-dataset-converter
cp ../data/mevsimler_iklim_veriseti.csv ./
git add .
git commit -m "İlk veri seti eklendi."
git push
```

---

## Katkıda Bulunanlar

* [@abdbali](https://github.com/abdbali)

---

## Lisans

Bu proje [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) ile lisanslanmıştır.

---

## English Version

### Purpose

**Educational Dataset Converter** is an open source project designed to transform educational texts (e.g., textbooks, curriculum documents) into clean `"input", "output"` formatted datasets suitable for training NLP and LLM applications.

Datasets are published openly via [Hugging Face Datasets](https://huggingface.co/datasets/abdbali).

### Installation

```bash
pip install pandas datasets huggingface_hub
```

### Usage

```bash
python scripts/convert_to_csv.py --input source.txt --output data/output.csv
```

### Example Output

```csv
"input","output"
"What is climate?","It is the average of weather events observed over a long period in a region."
```

### Upload to Hugging Face

```bash
huggingface-cli login
huggingface-cli repo create abdbali/educational-dataset-converter
```

---

**Educational Dataset Converter** is licensed under Apache License 2.0.
