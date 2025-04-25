def get_book_text(filepath):
   with open(filepath) as f:
        file_contents = f.read()
   return file_contents

def get_word_count(text):
    return len(text.split())

def get_character_counts(text):
    char_counts = {}
    for char in text.lower() :
        if char not in  char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_on(dict):
    return dict["num"]
    
def to_list(dict):
    list = []
    for key in dict:
        list.append({"char":key,"num":dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list

def print_report_on(filepath):
    file_path = filepath
    book = get_book_text(filepath)
    count = get_word_count(book)
    chars = get_character_counts(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_dict in to_list(chars):
        char = char_dict["char"]
        num = char_dict["num"]
        if(char.isalpha()):
         print(f"{char}: {num}")
    print("============= END ===============")