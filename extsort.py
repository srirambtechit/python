def extsort(list):
 list.sort(key = lambda s:s[s.index('.') + 1 : len(s)])

l = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print l
extsort(l)
print l
