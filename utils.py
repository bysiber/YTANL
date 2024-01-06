import json

def read_json(path='data.json'):
    with open(path, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def read_text(file='data.txt', clean=True):
    lines = []
    with open(file, encoding="utf-8") as f:
        #read line by line
        for line in f:
            if clean : line = get_clean_text(line)
            if line is not None:
                lines.append(line)
            else:
                pass
    return lines

def get_clean_text(text):
    # Remove newline characters and strip leading/trailing whitespace
    text = text.replace('\n', '')
    text = text.strip()
    if text == "": return None
    return text


def get_sentences(data=None,path='data.txt'):
    if data == None: 
        lines = read_text(path, clean=True)
    else:
        lines = []
        for line in data:
            line = get_clean_text(line)
            if line is not None:
                lines.append(line)
            else:
                pass
    return lines

