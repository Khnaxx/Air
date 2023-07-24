
import air00, air01, air02, air03, air04, air05, air06, air07, air08, air09, air10, air11, air12

total = 0
nb_test = 13

if air00.display_text_split("Bonjour les gars") == ["Bonjour","les","gars"]:
    print("\033[0;032mair00 (1/1) : success")
    total += 1
else: print("\033[0;031mair00 (1/1) : failure")

if air01.display_text_split("Crevette magique dans la mer des étoiles", "la") == ["Crevette magique dans "," mer des étoiles"]:
    print("\033[0;032mair01 (1/1) : success")
    total += 1
else: print("\033[0;031mair01 (1/1) : failure")

if air02.display_text_concat(["je","teste","des","trucs"], " ") == "je teste des trucs":
    print("\033[0;032mair02 (1/1) : success")
    total += 1
else: print("\033[0;031mair02 (1/1) : failure")

if air03.display_not_double([1,2,3,4,5,4,3,2,1]) == 5:
    print("\033[0;032mair03 (1/1) : success")
    total += 1
else: print("\033[0;031mair03 (1/1) : failure")

if air04.display_correct_sentence("Hello milady,    bien ou quoi ??") == "Helo milady, bien ou quoi ?":
    print("\033[0;032mair04 (1/1) : success")
    total += 1
else: print("\033[0;031mair04 (1/1) : failure")

if air05.display_result_arr([1,2,3,4,5],"+2") == [3,4,5,6,7]:
    print("\033[0;032mair05 (1/1) : success")
    total += 1
else: print("\033[0;031mair05 (1/1) : failure")

if air06.display_caract_not_inside(["Michel","Albert","Thérèse","Benoit"],"t") == ["Michel"]:
    print("\033[0;032mair06 (1/1) : success")
    total += 1
else: print("\033[0;031mair06 (1/1) : failure")

if air07.sorted_insert([1,3,4],2) == [1,2,3,4]:
    print("\033[0;032mair07 (1/1) : success")
    total += 1
else: print("\033[0;031mair07 (1/1) : failure")

if air08.sorted_fusion([10,20,30],[15,25]):
    print("\033[0;032mair08 (1/1) : success")
    total += 1
else: print("\033[0;031mair08 (1/1) : failure")

if air09.shift_left(["Michel","Albert","Thérèse","Benoit"]) == ["Albert","Thérèse","Benoit","Michel"]:
    print("\033[0;032mair09 (1/1) : success")
    total += 1
else: print("\033[0;031mair09 (1/1) : failure")

if air10.show_file("a.txt"):
    print("\033[0;032mair10 (1/1) : success")
    total += 1
else: print("\033[0;031mair10 (1/1) : failure")

if air11.pyramide([0,5]) == ['     0', '    000', '   00000', '  0000000', ' 000000000']:
    print("\033[0;032mair11 (1/1) : success")
    total += 1
else: print("\033[0;031mair11 (1/1) : failure")

if air12.quick_sort(["6","5","4","3","2","1"], 0, 5) == ['1', '2', '3', '4', '5', '6']:
    print("\033[0;032mair12 (1/1) : success")
    total += 1
else: print("\033[0;031mair12 (1/1) : failure")

print(f"Total success : {total}/{nb_test}")