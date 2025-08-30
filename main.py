from stats import get_books_text, get_word_count, get_char_count, sort_on
import sys

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    caminho_arquivo = sys.argv[1]
    texto = get_books_text(caminho_arquivo)
    num_words = get_word_count(texto)
    num_caracters = get_char_count(texto)


    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {caminho_arquivo}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_list =[]

    for char, num in num_caracters.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse = True, key=sort_on)

    for item in char_list:
        print(f"{item['char']}: {item['num']}")


main()

