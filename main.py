def main():
    # Relative filepath of the text of Frankstein, presuming running from ~/workspace/github.com/dcicio/bookbot
    path_to_file = "books/frankenstein.txt"
    
    file_contents = get_book_text(path_to_file)
    word_count = get_num_words(file_contents)
    final_count = get_letter_count(file_contents)

    print_report(final_count, word_count, path_to_file)

    
# Open and read the file into a variable
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Get the word count of a text string
def get_num_words(text):
    words = text.split()
    return len(words)

# For each character, we check if it's a letter
# If it is, we make sure it's lowercase
# Then we increment the value for the dictionary key of the letter
### CONFIRMED ACCURATE RESULTS
def get_letter_count(text):
    # This dictionary will hold the counts for each letter
    letter_count = {}

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # This goes through the alphabet letter by letter
    ## For each letter, it creates a key in the dictionary
    ## The value of each key is initialized to 0
    for character in alphabet:
        letter_count[character] = 0

    for character in text:
        if (character.isalpha()):
            character = character.lower()
            letter_count[character] += 1
    
    # Sorting the dictionary by key, in descending order
    sorted_letter_count = dict(sorted(letter_count.items(), key=lambda x:x[1], reverse=True))
    return sorted_letter_count

def print_report(counts, word_count, filepath):
    print(f"-- Begin report on {filepath} --")
    print()
    print(f"{word_count} words found in the document")
    print()

    for count in counts:
        print(f"The letter {count} appears {counts[count]} times")
    
    print()
    print("-- Thank you for using BookBot! --")

main()