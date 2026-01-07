from stats import num_words
from stats import character_qty
from stats import sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    #print(sys.argv)

    #Check for path to book
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_location = sys.argv[1]
    
    #Read file and save as string (Ch2, L3)
    book_text = get_book_text(book_location)

    #Print word count (Ch2, L4)
    #print (f"Found {num_words(book_text)} total words")

    #Count characters in text and print (Ch2, L6)
    characters_in_text = character_qty(book_text)
    #print (f't : " {characters_in_text["t"]}')
    #print (f'p : " {characters_in_text["p"]}')
    #print (f'c : " {characters_in_text["c"]}')
    #print (characters_in_text)

    #Sort character count (Ch3, L1)
    sorted_characters = sorted_list(characters_in_text)
    #print (sorted_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")

    for item in sorted_characters:
        if item["char"].isalpha() == True:
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()