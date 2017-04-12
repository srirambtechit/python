# python

##2. Working with Data

###2.1. Lists
$ [1, 2, 3]

$ range(1,5)
[1, 2, 3, 4]

$ a = [1, 2]

$ b = [3, 4]

$ a + b
[1, 2, 3, 4]

$ a * 3
[1, 2, 1, 2, 1, 2]

$ len(a)
2

$ a[1]
2

$ a[2] = 5
$ a
[1, 2, 5]

$ a[::-1] # reveres the list
[5, 2, 1]

$ a[1:2] # slices the list
[5, 2]

$ c = range(1, 6)
[1, 2, 3, 4, 5]

$ c[-3]
3

$ 5 in c
True

$ c.append(7)
[1, 2, 3, 4, 5, 7]

###2.1.1. The for Statement
'$ for x in [1, 2, 3, 4]:
'    print x

'$ for i  in range(10):
'    print i, i*i, i*i*i

# 2.1.2 Build-in functions
The built-in function zip takes two lists and returns list of pairs.
'$ zip(["a", "b", "c"], [1, 2, 3])
'[('a', 1), ('b', 2), ('c', 3)]

Ex:-
names = ["a", "b", "c"]
values = [1, 2, 3]
for name, value in zip(names, values):
    print name, value

$ sorted(list)
$ sorted(list, key=lambda n: n)


# 2.1.3 Sorting list
$ list.sort()
>>> a = ["hello", 1, "world", 45, 2]
>>> a.sort()
>>> a
[1, 2, 45, 'hello', 'world']
>>> a = [[2, 3], [1, 6]]
>>> a.sort()
>>> a
[[1, 6], [2, 3]]

optinally specify function as key
>>> a = [[2, 3], [4, 6], [6, 1]]
>>> a.sort(key=lambda x: x[1])
>>> a
[[6, 1], [2, 3],  [4 6]]

###2.7.2. Understanding Python Execution Environment

Python return all variables in the current environment
$ globals()
$ globals()['x']

Similarly to capture local variables (inside method)
$ locals()

