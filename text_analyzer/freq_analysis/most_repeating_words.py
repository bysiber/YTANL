import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def get_most_repeating_words(words, lang="english", max_num=100):
    # Stop words'leri kaldırma
    stop_words = set(stopwords.words('english'))  # İngilizce stop words'ler
    filtered_words = [word for word in words if word not in stop_words]

    # Kökleri almak için bir Stemmer oluşturma
    if lang == "english":
        stemmer = PorterStemmer()
        stems = [stemmer.stem(word) for word in filtered_words]

    # Frekans dağılımını hesaplama
    frequency = FreqDist(stems)

    # En çok tekrar eden kelimeleri bulma
    most_common_words = frequency.most_common(max_num)  # İlk 5 tekrar eden kelimeyi al
    print(most_common_words)
    # Sonuçları görüntüleme
    return dict(most_common_words)



