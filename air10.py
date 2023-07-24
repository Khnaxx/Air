import sys

def is_argument_valid(arg):
    if "." in arg and not "." in arg[-3]:
        return True
    else:
        print("error.")
        exit()

def show_file(file):
    fichier = open(file, "r")
    return fichier.read()
    fichier.close()

if __name__ == "__main__":
    file_name = sys.argv[1]

    if is_argument_valid(file_name):
        print(show_file(file_name))