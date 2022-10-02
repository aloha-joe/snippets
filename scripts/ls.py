import os

path = '/home/aloha/'


def filter_dir(is_file: bool) -> list:
    filtered_list = []
    with os.scandir(path) as list_of_entries:
        for entry in list_of_entries:
            if is_file:
                if entry.is_file():
                    filtered_list.append(entry.name)
            else:
                if entry.is_dir():
                    filtered_list.append(entry.name)
        return filtered_list


def head(list_of_entries):
    return list_of_entries[:5]


def filter_by_name(list_of_entries, some_string):
    for entry in list_of_entries:
        if some_string in entry:
            return entry


print(filter_dir(False))
print(head(os.listdir(path)))
print(filter_by_name(os.listdir(path), 'hist'))
