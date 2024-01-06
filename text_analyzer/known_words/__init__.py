from utils import read_json
import os

current_path = os.path.dirname(os.path.abspath(__file__)) #get current path

turkish_words = read_json(current_path + "\\" +"turkish.json")



lang_dict = {
    "turkish": turkish_words
}
def words_picker(lang, category="general"):
    return lang_dict[lang][category]