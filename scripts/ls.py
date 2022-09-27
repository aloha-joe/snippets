import os

path = '/home/aloha/'
directory_list = []
for i in os.listdir(path):
    directory_list += [i]

def filter_dir (is_file):
    filtered_list = []
    with os.scandir(path) as listOfEntries:
        if is_file == True:
            for entry in listOfEntries:
                if entry.is_file():
                    filtered_list += [entry.name]
        elif is_file == False:
            for entry in listOfEntries:
                if entry.is_dir():
                    filtered_list += [entry.name]
        return filtered_list
print(filter_dir(True))

def head(ListOfEntries):
    return ListOfEntries[:5]
print(head(directory_list))

def filter_by_name(ListOfEntries, some_string):
    for entry in ListOfEntries:
        if some_string in entry:
            return entry
print(filter_by_name(directory_list, 'hist'))