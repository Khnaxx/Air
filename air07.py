import sys

def is_argument_valid(arr, number):
    if len(arr) == 0 :
        return False
    else: return True

def sorted_insert(arr,adding_number):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] < adding_number:
            new_arr.append(arr[i])
        else:
            new_arr.append(adding_number)
            new_arr.extend(arr[i:])
            return new_arr

if __name__ == "__main__":
    table = sys.argv[1:-1]
    number = sys.argv[-1]

    if is_argument_valid(table,number):
        for arg in sorted_insert(table,number):
            print(arg,end = " ")
