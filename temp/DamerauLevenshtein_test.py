from textdistance import DamerauLevenshtein
"""
Bu kod parçası, textdistance kütüphanesinin DamerauLevenshtein sınıfını kullanarak 
iki metin arasındaki benzerliği hesaplar. İlk olarak, bir DamerauLevenshtein nesnesi 
oluşturulur. Sonra 'video' ve 'videos' gibi iki örnek metin alınır. 
iki metin arasındaki benzerlik puanı, normalized_similarity metodu ile hesaplanır 
ve sonuç 0 ile 1 arasında bir değer olarak döner. 
Eğer bu puan belirlenen eşik değeri olan 0.5'ten büyük veya eşitse, 
iki metnin benzer olduğu kabul edilir. Bu kod parçası benzerlik puanını 
hesaplar ve sonucu ekrana basar.
"""

# Initialize the DamerauLevenshtein object
damerau_levenshtein = DamerauLevenshtein()

# Test strings
string1 = 'video'
string2 = 'videos'

# Calculate the normalized similarity
threshold = 0.5
similarity_score = damerau_levenshtein.normalized_similarity(string1, string2)

print(f'The similarity score between "{string1}" and "{string2}" is {similarity_score}')

