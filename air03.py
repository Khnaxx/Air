import sys

def is_argument_valid(arr):
    if len(arr) < 3:
        return False
    else : return True

def display_not_double(arr):
    for i in range(len(arr)):
        if not arr[i] in arr[i+1:]:
            return(arr[i])


if __name__ == "__main__":
    table = sys.argv[1:]
    if is_argument_valid(table):
        print(display_not_double(table))
    else: print("error.")
