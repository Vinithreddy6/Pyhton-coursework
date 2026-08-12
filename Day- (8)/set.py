Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#SET
#mu unord

#doesn't allow duplicates
s=set()
type(s)
<class 'set'>
s={,2,3,4,5,66,67.5}
SyntaxError: invalid syntax
s={1,2,3,45,65,78.4}
s
{1, 2, 3, 65, 45, 78.4}
s={1,1,2,2}
s
{1, 2}
s.add(3)
s
{1, 2, 3}
s.add(12.3)
s.add('str')
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,2,3})
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.add({1,2,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
s.add({1:2,2:3})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.add({1:2,2:3})
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
s.add(True)
s
{1, 2, 3, 12.3, 'str'}
s.add(False)
s
{False, 1, 2, 3, 12.3, 'str'}
#WE CANNOT PERFORM + OR slicing operations
#but:
a={1,2,3,4,5}
b={3,4,5,6}
1 in a
True
3 in b
True
a
{1, 2, 3, 4, 5}
a|b
{1, 2, 3, 4, 5, 6}
a&b
{3, 4, 5}
a-b
{1, 2}
b-a
{6}
{1}<=a
True
{1,6}<=a
False
a>{1,2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a>={1,3}
True
a>={1,7}
False

m={1,2,3}
n={4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(m)
False
#methods:
a={12,34,10,40,5}
sorted(a)
[5, 10, 12, 34, 40]
>>> a.count(12)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.count(12)
AttributeError: 'set' object has no attribute 'count'
>>> sum(a)
101
>>> all({12,34})
True
>>> any({'True',12})
True
>>> a.add(5)
>>> a
{34, 5, 40, 10, 12}
>>> c=a.copy()
>>> c
{34, 5, 40, 10, 12}
>>> c.add(4)
>>> c
{34, 4, 5, 40, 10, 12}
>>> a
{34, 5, 40, 10, 12}
>>> a.update(6,100,111)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.update(6,100,111)
TypeError: 'int' object is not iterable
>>> a.update({6,100})
>>> a
{34, 100, 5, 6, 40, 10, 12}
>>> a.remove(100)
>>> a
{34, 5, 6, 40, 10, 12}
>>> a.pop()
34
>>> a.pop()
5
>>> a
{6, 40, 10, 12}
>>> a.discard(12)
>>> a
{6, 40, 10}
>>> a.clear()
>>> a
set()
