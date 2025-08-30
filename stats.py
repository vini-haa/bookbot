def get_books_text(caminho_arquivo):
    with open(caminho_arquivo) as f:
        return f.read()

def get_word_count(texto):
    palavras = texto.split()
    return len(palavras)

def get_char_count(texto):
    chars = {}
    for c in texto.lower():
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    return chars

def sort_on(item):
    return item["num"]
