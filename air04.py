import sys

def is_argument_valid(arr):
    if not len(arr) == 2:
        return False
    else: return True

def display_correct_sentence(sentence):
    correct_sentence = sentence[0]
    for i in range(1,len(sentence)):
        if not sentence[i] == correct_sentence[-1]:
            correct_sentence += sentence[i]
    return correct_sentence

if __name__ == "__main__":
    table = sys.argv
    if is_argument_valid(table):
        print(display_correct_sentence(table[-1]))
    else: print("error.")
