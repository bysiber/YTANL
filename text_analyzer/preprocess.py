from textdistance import DamerauLevenshtein
from utils import read_json
from text_analyzer.known_words import turkish_words, words_picker
from text_analyzer.text_similarity import Damerau_Levenshtein
from text_analyzer.freq_analysis import freqAnalysis
import nltk

class Preprocess():
    
    def __init__(self,lang="turkish"):
        """
        Bu fonksiyon, nesneyi başlatmak için kullanılır. İstenen dili
        ayarlar ve o dile ait genel kategorideki kelimeleri seçer.
        Ayrıca, cümleleri saklamak için boş bir liste oluşturur.

        Parametreler:
        lang (str): Kullanılacak dil. Eğer belirtilmezse varsayılan
                    dil olarak "turkish" seçilir.
        """
        self.lang = lang
        self.known_words = words_picker(self.lang, category="general")
        self.chat_messages = [] # it will be a list of messages (min 1 sentence)

    def reset_data(self): 
        """
        Nesnenin 'sentences' özelliğini temizler ve yeni bir boş liste
        atayarak nesneyi başlangıç durumuna getirir.
        """
        self.chat_messages = []

    def set_data(self, path):
        """
        Dosya yolundan veriyi okur ve 'sentences' özelliğine dönüştürülmüş 
        haliyle atar. Veriyi dönüştürmek için 'get_basic_sentences' 
        fonksiyonunu kullanır.
        
        Parametreler:
        - path: Okunacak verinin dosya yolu.
        """
        self.chat_messages = read_json(path=path)

    def get_messages(self, path):
        return self.chat_messages


    def _correct_message(self, message, known_words, threshold=0.4, full_check=False):
        """
        Cümleyi düzeltir ve tanınan kelimelerle eşleşmesini sağlar.
        Eşik değeri ve tam kontrol opsiyonu ile esneklik sağlar.

        Parametreler:
        - sentence: Düzeltilecek cümle (string).
        - known_words: Bilinen kelimelerin listesi.
        - threshold: Benzerlik için eşik değeri (varsayılan 0.4).
        - full_check: Tüm bilinen kelimelerle karşılaştırma yapılıp 
                      yapılmayacağını belirten bool (varsayılan False).

        Döndürdüğü Değer:
        - Düzeltme sonrası oluşan cümle (string).
        """
        words = message["content"]["message"].split()
        corrected_words = []
        similar_word = ""
        for word in words:
            similar_word = word # If no similar word is found, return the original word
            for known_word in known_words:
                if Damerau_Levenshtein(word, known_word):
                    similar_word = known_word
                    if not full_check: break
                    else: pass
        
            corrected_words.append(similar_word)
        return " ".join(corrected_words)

    def correct_messages(self, messages=None, known_words=None, threshold=0.4, full_check=False):
        """
        Birden fazla cümleyi düzeltir ve bilinen kelimelerle eşleştirir.
        Opsiyonel olarak eşik değeri ve tam kontrol sağlar.

        Parametreler:
        - sentences: Düzeltilecek cümleler listesi (varsayılan None).
        - known_words: Bilinen kelimelerin listesi (varsayılan None).
        - threshold: Benzerlik için eşik değeri (varsayılan 0.4).
        - full_check: Tüm bilinen kelimelerle karşılaştırma yapılıp 
                      yapılmayacağını belirten bool (varsayılan False).

        Eğer 'sentences' veya 'known_words' None olarak belirtilirse,
        nesnenin mevcut 'sentences' veya 'known_words' özellikleri
        kullanılır. Düzeltme sonrasında 'sentences' özelliği güncellenir.
        """
        if messages == None: 
            messages = self.chat_messages

        if known_words == None: 
            known_words = self.known_words

        corrected_messages= []
        for message in messages:
            corrected_messages.append(self._correct_message(message["content"]["message"], known_words))
        self.message = corrected_messages

    def tokinize(self, message):
        """
        Verilen metni kelimelere ayırarak 'tokenize' eder.

        Parametreler:
        - text: Tokenize edilecek metin (string).

        İşlev, 'nltk' kütüphanesinin 'word_tokenize' metodunu kullanarak
        İngilizce dilinde metni kelimelere ayırır ve token listesi olarak
        döndürür.
        
        Döndürdüğü Değer:
        - tokens: Metnin token haline getirilmiş listesi.
        """
        tokens = nltk.word_tokenize(message, language='english') # tokens = words
        return tokens
    
    def pos_tag(self, tokens):
        """
        Verilen token'ların (kelimelerin) sözdizimsel kategorilerini etiketler.

        Parametreler:
        - tokens: Sözdizimi etiketlemesi yapılacak token'ların listesi.

        İşlev, 'nltk' kütüphanesinin 'pos_tag' metodunu kullanarak
        token'ları (kelimeleri) Part-of-Speech (POS) etiketlerine göre 
        etiketler ve bu etiketlenmiş çiftlerin listesini döndürür.
        
        Döndürdüğü Değer:
        - Etiketlenmiş token'lar: Her bir kelime için (token, etiket) 
          formundaki çiftlerin listesi.
        """
        return nltk.pos_tag(tokens)

    def name_entity_recognition(self, tagged_tokens):
        """
        Etiketlenmiş kelimelerden isim varlıklarını tanır ve ayırır.

        Parametreler:
        - tagged: Part-of-Speech etiketlenmiş kelime çiftlerinin listesi.

        İşlev, nltk'nin 'ne_chunk' metodunu kullanarak etiketlenmiş
        kelimeler içindeki isim varlıklarını tanır. Özel isim varlıkları ve
        özel olmayan isim varlıkları ayrı listelerde saklanır ve her iki
        liste de geri döndürülür.
        
        Döndürdüğü Değerler:
        - tags: ne_chunk tarafından döndürülen ağaç yapısı.
        - entities: Özel isim varlıklarının listesi.
        - non_entities: Özel olmayan varlıkların listesi.
        """
        tags = nltk.chunk.ne_chunk(tagged_tokens)
        non_entities = []
        entities = []
        for entity in tags:
            if hasattr(entity, 'label'):
                #burda sadece ozel varlıkları yazdırıyoruz
                for c in entity:
                    ent = {
                        "entity": c[0],
                        "label": entity.label()
                    }
                    entities.append(ent)
            else:
                # burda sadece ozel olmayan varlıkları yazdırıyoruz
                non_entities.append(
                    {
                        "entity": entity[0],
                        "label": entity[1]
                    }
                )

        return tags, entities, non_entities
        
    ######### freq analysis functions ########

    def get_most_repeating_words(self):
        content = []
        for message in self.chat_messages:
            if "message" in message["content"]:
                content.append(message["content"]["message"])
        
        words = self.tokinize(" ".join(content))
        most_repeating_words = freqAnalysis.get_most_repeating_words(words)
        return most_repeating_words

    def get_most_active_authors(self):
        content = []
        for message in self.chat_messages:
            content.append({"author": message["author"], "timeStamp": message["occurence_timestamp"]})
        
        most_active_authors = freqAnalysis.get_most_active_authors(content)
        return most_active_authors

    def get_spent_time_authors(self):
        content = []
        for message in self.chat_messages:
            content.append({"author": message["author"], "timeStamp": message["occurence_timestamp"]})
        
        spent_time_authors = freqAnalysis.get_spent_time_authors(content)
        return spent_time_authors
        


        
    def _run(self, path=None):
        if path != None: self.read_data(path)
        print(self.messages)
        self.correct_messages(known_words=words_picker(self.lang, category="general"))
        print(self.messages)

if __name__ == "__main__":
    #message["content"]["message"]
    proc = Preprocess()
    text = "im co-founder of the Github company in Middle-East, but i'd love to work in the Istanbul as a ceo of the Amazon company."
    tokens = proc.tokinize(text)
    tagged = proc.pos_tag(tokens)
    tags, entities, non_entities = proc.name_entity_recognition(tagged)


