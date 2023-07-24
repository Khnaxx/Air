import sys

def display_text_split(string_to_cut):
    caract_separation = " "
    begin = 0
    string_separate = []
    for i in range(len(string_to_cut)):
        if string_to_cut[i] == caract_separation:
            string_separate.append(string_to_cut[begin:i])
            begin = i+1
        elif i == len(string_to_cut)-1:
            string_separate.append(string_to_cut[begin:])
    return string_separate

def is_argument_valid(arr):
    if len(arr) == 0:
        return False
    else: return True


if __name__ == '__main__':
    table = sys.argv[1:]
    if is_argument_valid(table):
        for arg in display_text_split(table[0]):
            print(arg)
    else : print("error.")
