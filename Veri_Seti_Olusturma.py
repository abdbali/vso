import pandas as pd
import os
from IPython.display import HTML, display
import base64
data_1 = [
    ["21 Mart’ta kuzey yarım kürede hangi mevsim başlar?", "İlkbahar"],
    ["21 Mart’ta güney yarım kürede hangi mevsim başlar?", "Sonbahar"],
    ["21 Mart’ta gece ve gündüz süreleri nasıldır?", "Eşittir, 12 saat"],
    ["21 Mart’ta güneş ışınları nereye dik düşer?", "Ekvatora"],]
data_2 = [
    ["İklim nedir?", "Yeryüzünün bir kısmında uzun yıllar boyunca gözlenen hava olaylarının ortalamasıdır."],
    ["Dünyanın farklı bölgelerinde hangi iklim çeşitleri gözlemlenir?", "Kutup, ekvatoral, karasal, çöl iklimi gibi iklim çeşitleri gözlemlenir."],
    ["Türkiye’de hangi iklim tipleri görülür?", "Akdeniz, Karadeniz ve karasal iklim."],
    ["İklimle ilgilenen bilim dalı nedir?", "Klimatoloji"],]
combined_data = data_1 + data_2
df = pd.DataFrame(combined_data, columns=["input", "output"])
combined_data = data_1 + data_2
df = pd.DataFrame(combined_data, columns=["input", "output"])
file_path = "/mnt/data/mevsimler_iklim_veriseti.csv"
output_dir = os.path.dirname(file_path)
if not os.path.exists(output_dir):
    try:
        os.makedirs(output_dir)
        print(f"Dizin oluşturuldu: {output_dir}")
    except OSError as e:
        print(f"Hata: Dizin oluşturulamadı {output_dir}. Lütfen izinleri kontrol edin. Hata detayı: {e}")
        raise
else:
    print(f"Dizin zaten mevcut: {output_dir}")
try:
    df.to_csv(file_path, index=False)
    print(f"Dosya başarıyla kaydedildi: {file_path}")
    def create_download_link(filepath, title="Dosyayı İndir"):
        with open(filepath, "rb") as f:
            file_content = f.read()
        b64 = base64.b64encode(file_content).decode()
        file_name = os.path.basename(filepath)
        href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">{title}</a>'
        return href
    download_link_html = create_download_link(file_path, title="CSV Dosyasını İndir")
    display(HTML(download_link_html))
except OSError as e:
    print(f"Hata: Dosya kaydedilemedi veya okunamadı {file_path}. Lütfen dizin izinlerini kontrol edin veya yolun doğru olduğundan emin olun. Hata detayı: {e}")
except Exception as e:
    print(f"Beklenmedik bir hata oluştu: {e}")
print(f"Kayıt yolu: {file_path}")
