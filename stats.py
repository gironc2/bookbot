def num_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def character_qty (text):
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on (items):
    return items["num"]

def sorted_list (char_dict):
    char_dict_list = []
    for k in char_dict:
        char = k
        num = char_dict[k]
        temp_dict = {
            "char" : char,
            "num" : num
        }
        char_dict_list.append(temp_dict)
        #print (f'adding {temp_dict} to list')
    #check = char_dict_list.sort(reverse=True, key=sort_on)
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list
    #print (check)
    #return "printed"