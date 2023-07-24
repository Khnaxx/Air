import sys

def is_argument_valid(table):
    for i in range(len(table)):
        if table[i] == "fusion":
            index = i
            return table[:i],table[i+1:]
    else:
        return False

def sorted_fusion(arr1,arr2):
    arr_fusion = arr1 + arr2
    for i in range(len(arr_fusion)-1,1,-1):
        for j in range(0,i):
            if arr_fusion[j+1] < arr_fusion[j]:
                arr_fusion[j+1], arr_fusion[j] = arr_fusion[j], arr_fusion[j+1]
    return arr_fusion

if __name__ == "__main__":
    table = sys.argv[1:]
    if is_argument_valid(table):
        first_arr, second_arr = is_argument_valid(table)
        print(sorted_fusion(first_arr,second_arr))

