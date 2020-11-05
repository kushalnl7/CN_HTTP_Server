import datetime
def getdate(s):
    k = []
    p = s.split(',')
    print(p)
    for i in p:
        print(int(i))
        k.append(int(i))
    return k


s = "2009, 12, 2, 10, 24, 34, 198130"
p = getdate(s)
a = datetime.datetime(p[0], p[1], p[2], p[3], p[4], p[5], p[6])
b = datetime.datetime(2009, 12, 2, 10, 24, 36, 910128)
print(a>b)