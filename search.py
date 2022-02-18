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

#bad sign heuristic
def bad_char(string):
    size = len(string)

    bad = {}
    for i in range(size-1):
        bad[(string[i])] = i

    return bad

#good prefix heuristic
def good_suf(string):
    size = len(string)

    index_ele = size #start from end
    initial_place = size +1

    main_table = [0]*initial_place  #create a clear list of zeros
    support_table = [None]*initial_place    #create a list of nones

    support_table[index_ele] = initial_place    #initiate the last element of the list

    while index_ele > 0:
        while (initial_place <= size) and (string[index_ele -1] != string[initial_place - 1]): #deal with existing pre-suf-ix case or cant be expanded
            if main_table[initial_place] == 0:
                main_table[initial_place] = initial_place -1
            initial_place = support_table[initial_place] # set the inner pre-suf-iks
        
        initial_place = initial_place -1 #the pre-suf-iks is expandable or doesnt exist
        index_ele = index_ele -1
        support_table[index_ele] = initial_place # save the position of the pre_suf_iks
    
    initial_place = support_table[0]
    for i in range(0, size +1):
        if main_table[i] == 0:  #in free spaces put the position of the pre-suf-iks
            main_table[i] = initial_place
        if i == initial_place:  #if the pre-suf-iks doesn't have the pre-suf-iks, take the next one
            initial_place = support_table[initial_place]

    return main_table
        


def find_boyer(string, text):
    listed = [] 
    if (string == "") or (len(string)> len(text)):  #check if string is empty or is text is shorter than string
        return listed
    Bad = bad_char(string)  #load bad character table
    Good = good_suf(string) #load good prefix table
    
    found = -1      #set the position of the string in the text to "not yet found"
    index = 0       #set the frame of the string to the beginning of the text

    while index <= (len(text) - len(string)):   #as long as the frame fits in the text
            compared_index = len(string) -1
            while (compared_index > -1) and (string[compared_index] == text[index + compared_index]):   #if the characters are the same
                compared_index = compared_index -1
                if compared_index == -1:    #if the whole substring fits the frame
                    found = index
                    listed.append(found)    #append the index 
            if text[index + compared_index] in Bad: #move the frame by either the fitting sufix move or the bad character move
                index = index + max(Good[compared_index +1], compared_index - Bad[text[index + compared_index]])
            else:   #if the letter is not in the bad characters move either by the good suffix or by full length
                index = index + max(Good[compared_index +1], compared_index + 1)

    if found == -1:
        return listed
    return listed




