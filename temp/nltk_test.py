import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import words

# NLTK'nin sözlüğünü yükle
nltk.download('words')

# Verilen metin
text_A = "inşal sport bakanı bugün sniemada düşmemiştir yoksa insanlar üzülür"

# Türkçe kelimelerin bulunduğu sözlüğü kullan
turkish_words = set(words.words())

# Metni kelimelere ayır
tokens = word_tokenize(text_A)

# Kelimeleri kontrol edip eğer sözlükte yoksa düzelt
corrected_text = ' '.join([word if word in turkish_words else 
                           max(((w, nltk.edit_distance(word, w)) for w in turkish_words), key=lambda x: x[1])[0] 
                           for word in tokens])

print("Düzeltildi:")
print(corrected_text)