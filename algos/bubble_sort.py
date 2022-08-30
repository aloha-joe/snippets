def sort(a):
    s = 0
    for _ in range(len(a) - 1):
        for i in range(len(a) - 1):
            while a[i] < a[i + 1]:
                s = a[i]
                a[i] = a[i + 1]
                a[i + 1] = s
    return (a)

