import sys

def display_text_split(string_to_cut,caract_separation):
    len_caract_separation = len(caract_separation)
    string_separate = []
    for i in range(0,len(string_to_cut)):
        if string_to_cut[i:i+len_caract_separation] == caract_separation:
            string_separate.append(string_to_cut[:i])
            string_separate.append(string_to_cut[i+len_caract_separation:])
            return string_separate


def is_argument_valid(arr,separation):
    if not separation in arr: 
        return False
    else: return True

if __name__ == '__main__':
    table = sys.argv[1]
    separation = sys.argv[-1]
    if is_argument_valid(table,separation):
        for arg in display_text_split(table,separation):
            print(arg)
    else: print("error.")
