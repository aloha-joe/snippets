with open('/home/aloha/Projects/test.txt') as inf:
    s1 = inf.readline().strip()
    s2 = inf.readline().strip()

with open('/home/aloha/Projects/test.txt', 'a') as ouf:
    ouf.write(f"{s2}\n{s1}")
