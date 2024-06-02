import csv
from nltk.corpus import wordnet as wn
import nltk

# Gerekli dosyaları indir
nltk.download('wordnet')

input_file = 'kelimeler.csv'
output_file = 'kelimeler_ve_anlamlari.csv'

def get_meaning(word):
    synsets = wn.synsets(word)
    if synsets:
        # İlk synset'in tanımını al
        return synsets[0].definition()
    else:
        return 'Anlam bulunamadı'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Başlık satırını yaz
    header = next(reader)
    header.append('Anlamı')
    writer.writerow(header)

    for row in reader:
        kelime = row[0]
        seviye = row[1]
        
        try:
            anlam = get_meaning(kelime)
        except Exception as e:
            anlam = 'Hata: ' + str(e)
        
        row.append(anlam)
        writer.writerow(row)
