import sys

def is_argument_valid(arr):
    if len(arr) == 0:
        return False
    else : return True

def shift_left(arr):
    shift = 1
    shift_arr = []
    shift_arr += arr[int(shift):]
    shift_arr +=arr[:int(shift)]
    
    return shift_arr

if __name__ == "__main__":
    table = sys.argv[1:]

    if is_argument_valid(table):
        for arg in shift_left(table):
            print(arg, end = " ")
    else: print("error.")
