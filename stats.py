def get_num_words(text):
    words = text.split()
    return len(words)

def get_character(text):
    char = text.split()
    return len(char)  

def get_character_count(text):
    counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char in counts:
                counts[char] += 1 
            else:
                counts[char] = 1
    return counts
       
#transform counts dictionary into a list of small dictionaries {"char": "e", "num": 44538}
def list_of_dicts(counts):
    new_dicts = []
    for char, count in counts.items(): 
        new_dicts.append({"char": char, "num": count})
    return new_dicts

 #returns the value of the "num" key in the dictionary
def sort_on_num(dictionary):
    return dictionary["num"]

#sort your list of dictionaries by the "num" value
#not printing in sorted order, new_dicts or what#
def sorted_list(new_dicts):
    new_dicts.sort(reverse=True, key=sort_on_num) #sorts the list in place
    return new_dicts #returns the sorted list






   


