import itertools

word_list = []
word_dict = {}
with open('/home/aloha/Projects/you_know_my_name.txt') as inf:
    for line in inf:
        line = (line.replace('?', '').replace('(', '').replace(')', '').replace('!', '').replace('.', '').split())
        for i in line:
            word_list.append(i.lower())
for x in word_list:
    if x not in word_dict:
        word_dict[x] = word_list.count(x)
sorted_word_dict = dict(sorted(word_dict.items(), key=lambda item: -item[1]))
for key, value in itertools.islice(sorted_word_dict.items(),20):
    print(f'{"|"}{key:>21}{"|"} {value:>10}{"|"}')