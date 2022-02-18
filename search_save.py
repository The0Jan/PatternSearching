def find_naive(string, text):
    string_len = len(string)
    text_len = len(text)
    listed = []
    if string == "":
        return listed
    for i in range(text_len - string_len + 1):
        if string == text[i:i+string_len]:

            listed.append(i)
    return listed


def bad_char(string):
    size = len(string)
    number_of_characters = 256

    bad = [-1]*number_of_characters
    for i in range(size-1):
        bad[ord(string[i])] = i

    return bad


def good_suf(string):
    size = len(string)

    index_ele = size
    initial_place = size +1

    main_table = [0]*initial_place
    support_table = [None]*initial_place

    support_table[index_ele] = initial_place

    while index_ele > 0:
        while (initial_place <= size) and (string[index_ele -1] != string[initial_place - 1]):
            if main_table[initial_place] == 0:
                main_table[initial_place] = initial_place -1
            initial_place = support_table[initial_place]
        
        initial_place = initial_place -1
        index_ele = index_ele -1
        support_table[index_ele] = initial_place
    
    initial_place = support_table[0]
    for i in range(0, size +1):
        if main_table[i] == 0:
            main_table[i] = initial_place
        if i == initial_place:
            initial_place = support_table[initial_place]

    return main_table
        


def find_boyer(string, text):
    listed = [] 
    if (string == "") or (len(string)> len(text)):
        return listed
    Bad = bad_char(string)
    Good = good_suf(string)
    
    found = -1
    index = 0

    while index <= (len(text) - len(string)):
            compared_index = len(string) -1
            while (compared_index > -1) and (string[compared_index] == text[index + compared_index]):
                compared_index = compared_index -1
                if compared_index == -1:
                    found = index
                    listed.append(found)
            index = index + max(Good[compared_index +1], compared_index - Bad[ord(text[index + compared_index])])
    if found == -1:
        return listed
    return listed




