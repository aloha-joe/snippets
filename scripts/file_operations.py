with open('/home/aloha/Projects/test.txt') as inf:
    s1 = inf.readline().strip()
    s2 = inf.readline().strip()

with open('/home/aloha/Projects/test.txt', 'a') as ouf:
    ouf.write(s2)
    ouf.write('\n')
    ouf.write(s1)