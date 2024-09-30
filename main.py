def main():
    # Relative filepath of the text of Frankstein, presuming running from ~/workspace/github.com/dcicio/bookbot
    path_to_file = "books/frankenstein.txt"
    
    # Opening and reading the file into a variable
    with open(path_to_file) as f:
        file_contents = f.read()
    
    # Printing the text to console
    print(file_contents)

main()