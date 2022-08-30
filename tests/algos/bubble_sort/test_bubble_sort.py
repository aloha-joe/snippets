import random
from algos import bubble_sort

test_list = [432, 6453, 312, 551, 1]
bubbled = bubble_sort.sort(test_list)
clean_sorted = sorted(test_list, reverse=True)
if bubbled == clean_sorted:
    print("Correct")
else:
    print("Incorrect")
