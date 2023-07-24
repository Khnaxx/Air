import sys

def display_text_concat(arr_to_concat,caract_concat):
    text = ""
    for i in arr_to_concat:
        if i != arr_to_concat[-1]:
            text += i
            text += caract_concat
        else: text += i
    return text


def is_argument_valid(arr, caract):
    if len(arr) < 4 or caract.isdigit(): 
        return False
    else: return True
    
if __name__ == '__main__':
    table = []
    for i in sys.argv[1:-1]:
        table.append(i)
    caract = sys.argv[-1]

    if is_argument_valid(table,caract):
        print(display_text_concat(table,caract))
    else : print("error.")
