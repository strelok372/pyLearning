import sys

o = sys.argv[1]
a = [',','.',' –',':','!','?']
for p in a:
    o = o.replace(p, '')
o = o.lower()
o = o.split(' ')
# p = '-'
# print(a.__contains__(p))
con = 0
wor = ''
for i in o:
    if (o.count(i) > con):
        wor = i
        con = o.count(i)
#     print(i)
    # if (i == ',') or (i == '.'):

# print(wor + ' meets ' + str(con) + ' times!')

print(int(','))
# print(o)
# for i in o:
    # print(i)