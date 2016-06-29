import sys
amt = int(sys.stdin.readline())
for case in range(amt):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keyword = sys.stdin.readline()
    new_keyword = ''
    char_list = []
    for character in keyword:
        if character not in char_list:
            char_list.append(character)
    
    char_list.remove("\n")
    
    for character in char_list:
        new_keyword+=character
    for character in char_list:
        alphabet = alphabet.replace(character, "")
    
    decode_list = []
    decode_list.append(new_keyword)
    decode_list.append("")
    row_count = 1
    row_length = len(char_list)
    for character in alphabet:
        if len(decode_list[row_count]) < row_length:
            decode_list[row_count] += character
            if len(decode_list[row_count]) == row_length:
                decode_list.append("")
                row_count = row_count + 1
    
    keyword_sort = "".join(sorted(new_keyword))
    column_list = []
    column_count = 0
    for char in keyword_sort:
        column_list.append("")
        place = new_keyword.find(char)
        for i in range(len(decode_list)):
            if len(decode_list[i]) > place:
                column_list[column_count] += decode_list[i][place]
        column_count = column_count + 1
        
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution = ""
    for row in column_list:
        sort = "".join(row)
        substitution += sort

    result = ''
    ciphertext = sys.stdin.readline()
    for char in ciphertext:
        if char == " ":
            result += " "
        elif char == "\n":
            pass
        else:
            result += alphabet2[substitution.find(char)]
    print result