import sys

def is_argument_valid(arr,caract):
    if len(arr) == 0 or len(caract) == 0:
        return False
    else: return True

def display_caract_not_inside(arr,caract):
    arr_pass = []
    for arg in arr:
        if not caract.lower() in arg.lower():
            arr_pass.append(arg)
    return arr_pass

if __name__ == "__main__":
    table = sys.argv[1:-1]
    caract = sys.argv[-1]

    if is_argument_valid(table,caract):
        for arg in display_caract_not_inside(table,caract):
            print(arg, end = ", ")
    else : print("error.")
