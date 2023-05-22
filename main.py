path_to_file = 'books/frankenstein.txt'

def word_count(text):
    words = text.split()
    return len(words)


def letter_count(text):
    lowered_text = text.lower()
    letter_dict = dict()

    for letter in lowered_text:
        if letter in letter_dict.keys():
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    return letter_dict

def report(file_path, text):
    number_of_words = word_count(text)
    letter_dict = letter_count(text)
    reverse_sorted_letter_dict = dict(sorted(letter_dict.items(), key=lambda x:x[1], reverse=True))

    print(f"--- Begin report of {file_path} ---")
    print(f"{number_of_words} found in the document\n")

    for character, count in reverse_sorted_letter_dict.items():
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")

    print("--- End report ---")

with open(path_to_file) as file:
    file_content = file.read()
    print(word_count(file_content))
    print(letter_count(file_content))
    report(path_to_file, file_content)
