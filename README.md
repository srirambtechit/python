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
$ for x in [1, 2, 3, 4]:
    print x

$ for i  in range(10):
    print i, i*i, i*i*i

# 2.1.2 Build-in functions
The built-in function zip takes two lists and returns list of pairs.
<code>
$ zip(["a", "b", "c"], [1, 2, 3])
[('a', 1), ('b', 2), ('c', 3)]

Ex:-
names = ["a", "b", "c"]
values = [1, 2, 3]
for name, value in zip(names, values):
    print name, value

$ sorted(list)
$ sorted(list, key=lambda n: n)
</code>

string functions:
<code>
>>> "hello world".split()
['hello', 'world']
>>> "a,b,c".split(',')
['a', 'b', 'c']

>>> " ".join(['hello', 'world'])
'hello world'
>>> ','.join(['a', 'b', 'c'])

>>> ' hello world\n'.strip()
'hello world'
>>> 'abcdefgh'.strip('abdh')
'cdefg'

>>> a = 'hello'
>>> b = 'python'
>>> "%s %s" % (a, b)
'hello python'
>>> 'Chapter %d: %s' % (2, 'Data Structures')
'Chapter 2: Data Structures'
</code>

dictionary functions:
<code>
>>> a = {'a': 1, 'b': 2, 'c': 3}
>>> a.keys()
['a', 'b', 'c']
>>> a.values()
[1, 2, 3]
>>> a.items()
{'a': 1, 'b': 2, 'c': 3}
>>> a.has_key('a')
True
>>> 'c' in a
True
>>> d = {'x': 1, 'y': 2, 'z': 3}
>>> d.get('x', 5)
1
>>> d.get('p', 5)
5
>>> d.setdefault('x', 0)
1
>>> d
{'x': 1, 'y': 2, 'z': 3}
>>> d.setdefault('p', 0)
0
>>> d
{'y': 2, 'x': 1, 'z': 3, 'p': 0}
>>> 'hello %(name)s' % {'name': 'python'}
'hello python'
>>> 'Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'}
'Chapter 2: Data Structures'
</code>


### 2.1.3 Sorting list
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

##2.2 Tuples
Tuple is a sequence type just like list, but it is immutable. A tuple consists of a number of values separated by commas.
>>> a = (1, 2, 3)
>>> a[0]
1

The enclosing braces are optional.

>>> a = 1, 2, 3
>>> a[0]
1
The built-in function len and slicing works on tuples too.

>>> len(a)
3
>>> a[1:]
2, 3
Since parenthesis are also used for grouping, tuples with a single value are represented with an additional comma.

>>> a = (1)
>> a
1
>>> b = (1,)
>>> b
(1,)
>>> b[0]
1

##2.3. Sets
Sets are unordered collection of unique elements.

>>> x = set([3, 1, 2, 1])
set([1, 2, 3])
Python 2.7 introduced a new way of writing sets.

>>> x = {3, 1, 2, 1}
set([1, 2, 3])
New elements can be added to a set using the add method.

>>> x = set([1, 2, 3])
>>> x.add(4)
>>> x
set([1, 2, 3, 4])
Just like lists, the existance of an element can be checked using the in operator. However, this operation is faster in sets compared to lists.

>>> x = set([1, 2, 3])
>>> 1 in x
True
>>> 5 in x
False


###2.7.2. Understanding Python Execution Environment

Python return all variables in the current environment
$ globals()
$ globals()['x']

Similarly to capture local variables (inside method)
$ locals()


##2.4. Strings
Strings also behave like lists in many ways. Length of a string can be found using built-in function len.

>>> len("abrakadabra")
11
Indexing and slicing on strings behave similar to that of lists.

>>> a = "helloworld"
>>> a[1]
'e'
>>> a[-2]
'l'
>>> a[:-2]
'hellowor'
>>> a[::-1]
'dlrowolleh'

The in operator can be used to check if a string is present in another string.

>>> 'hell' in 'hello'
True
>>> 'full' in 'hello'
False
>>> 'el' in 'hello'
True


##2.5. Working With Files
Python provides a built-in function open to open a file, which returns a file object
f = open('foo.txt', 'r') # open a file in read mode
f = open('foo.txt', 'w') # open a file in write mode
f = open('foo.txt', 'a') # open a file in append mode

>>> open('foo.txt').read()
'first line\nsecond line\nlast line\n'

>>> open('foo.txt').readlines()
['first line\n', 'second line\n', 'last line\n']
>>> f = open('foo.txt')
>>> f.readline()
'first line\n'
>>> f.readline()
'second line\n'
>>> f.readline()
'last line\n'
>>> f.readline()
''

>>> f = open('foo.txt', 'w')
>>> f.write('a\nb\nc')
>>> f.close()

>>> f.open('foo.txt', 'a')
>>> f.write('d\n')
>>> f.close()

##2.6. List Comprehensions
List Comprehensions provide a concise way of creating lists. Many times a complex task can be modelled in a single line.
<code>
>>> a = range(10)
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in a]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x*x for x in a]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x+1 for x in a]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

>>> a = range(10)
>>> [x for x in a if x % 2 == 0]
[0, 2, 4, 6, 8]
>>> [x*x for x in a if x%2 == 0]
[0, 4, 8, 36, 64]

>>> a = [1, 2, 3, 4]
>>> b = [2, 3, 5, 7]
>>> zip(a, b)
[(1, 2), (2, 3), (3, 5), (4, 7)]
>>> [x+y for x, y in zip(a, b)]
[3, 5, 8, 11]

>>> [(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0]
[(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (4, 0), (4, 2), (4, 4)]

>>> [(x, y) for x in range(5) for y in range(5) if (x+y)%2 == 0 and x != y]
[(0, 2), (0, 4), (1, 3), (2, 0), (2, 4), (3, 1), (4, 0), (4, 2)]

>>> [(x, y) for x in range(5) for y in range(x) if (x+y)%2 == 0]
[(2, 0), (3, 1), (4, 0), (4, 2)]
</code>

The following example finds all Pythagorean triplets using numbers below 25. (x, y, z) is a called pythagorean triplet if x*x + y*y == z*z.
<code>
>>> n = 25
>>> [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z]
[(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
</code>

##2.7. Dictionaries
Dictionaries are like lists, but they can be indexed with non integer keys also. Unlike lists, dictionaries are not ordered.
<code>
>>> a = {'x': 1, 'y': 2, 'z': 3}
>>> a['x']
1
>>> a['z']
3
>>> b = {}
>>> b['x'] = 2
>>> b[2] = 'foo'
>>> b[(1, 2)] = 3
>>> b
{(1, 2): 3, 'x': 2, 2: 'foo'}
</code>

The del keyword can be used to delete an item from a dictionary.
<code>
>>> a = {'x': 1, 'y': 2, 'z': 3}
>>> del a['x']
>>> a
{'y': 2, 'z': 3}
</code>






