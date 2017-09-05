# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
# new_list = ['hello','world']

def find_char(strarr, char):
    new_list = []
    for string in strarr:
        if string.find(char) != -1:
            new_list.append(string)
    return new_list
print find_char(word_list, char)
