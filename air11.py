import sys

def is_argument_valid(arg):
    if len(arg) == 2:
        return True
    else:
        return False

def pyramide(arr):
    stage = []
    caract = str(arr[0])
    height = int(arr[1])
    for i in range(height):
        stage.append(" " * (height - i) + caract * (i*2+1))
    return stage

if __name__ == "__main__":
    table = sys.argv[1:]
    if is_argument_valid(table):
        for stage in pyramide(table):
            print(stage)
            
    else: print("error.")
