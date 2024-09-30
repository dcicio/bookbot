def main():
    # This dictionary will hold the counts for each letter
    letter_count = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # This takes goes through the alphabet letter by letter
    ## For each letter, it creates a key in the dictionary
    ## The value of each key is initialized to 0
    for character in alphabet:
        letter_count[character] = 0
    
    # Relative filepath of the text of Frankstein, presuming running from ~/workspace/github.com/dcicio/bookbot
    path_to_file = "books/frankenstein.txt"
    
    file_contents = get_book_text(path_to_file)
    
    word_count = get_num_words(file_contents)

    print(f"{word_count} words found in the document")
    
# Open and read the file into a variable
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Get the word count of a text string
def get_num_words(text):
    words = text.split()
    return len(words)

main()