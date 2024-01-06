from textdistance import DamerauLevenshtein

"""
Bu kod parçası, textdistance kütüphanesinin DamerauLevenshtein sınıfını kullanarak 
iki metin arasındaki benzerliği hesaplar. İlk olarak, bir DamerauLevenshtein nesnesi 
oluşturulur. Sonra 'video' ve 'videos' gibi iki örnek metin alınır. 
iki metin arasındaki benzerlik puanı, normalized_similarity metodu ile hesaplanır 
ve sonuç 0 ile 1 arasında bir değer olarak döner. 
Eğer bu puan belirlenen eşik değeri olan 0.63'ten büyük veya eşitse, 
iki metnin benzer olduğu kabul edilir. Bu kod parçası benzerlik puanını 
hesaplar ve sonucu ekrana basar.
"""
def Damerau_Levenshtein(word1, word2, threshold=0.63, full_check=False):
    damerau_levenshtein = DamerauLevenshtein() # Create an instance of DamerauLevenshtein
    is_similar = damerau_levenshtein.normalized_similarity(word1, word2) > threshold
    return is_similar