from stats import get_num_words
from stats import get_character
from stats import get_character_count
from stats import list_of_dicts
from stats import sorted_list
from stats import sort_on_num
# Function to read the book text from a file
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Main function to orchestrate the program
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    character = get_character(text)
    counts = get_character_count(text)
    new_dicts = list_of_dicts(counts)
    #print(f"{num_words} words found in the document")
    #print(f"{counts} characters found in the document")
    #print(new_dicts)
    new_dicts.sort(reverse=True, key=sort_on_num) #sorts the list in place
    
    print(f"=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path}")
    print(f"---------- Word Count ---------")
    print(f"Found {num_words} total words")
    print(f"-------  Character Count ------")
    
    for item in new_dicts:
        print(f"{item['char']}: {item['num']}")
    print(f"============ END ==============")

main()
    
    