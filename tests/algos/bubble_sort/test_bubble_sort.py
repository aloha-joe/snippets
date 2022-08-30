import random
from algos import bubble_sort

test_list = [432, 6453, 312, 551, 1]
bubbled = bubble_sort.sort(test_list)
if bubbled == [6453, 551, 432, 312, 1]:
    print("Correct")
else:
    print("Incorrect")
