import sys

def is_argument_valid(arr,operation):
    if len(arr) == 0 or len(operation) == 1:
        return False
    else: return True

def display_result_arr(arr,operation):
    table = []
    operator, number = operation[0], int(operation[1:])
    if operator == "+":
        for i in arr:
            table.append(int(i) + number)
    elif operator == "-":
        for i in arr:
            table.append(int(i) - number)
    else: print("error.")
    return table

if __name__ == "__main__":
    table = sys.argv[1:-1]
    symbol = sys.argv[-1]

    if is_argument_valid(table,symbol):
        for arg in display_result_arr(table,symbol):
            print(arg,end = " ")
    else: print("error.")
                                         
    
