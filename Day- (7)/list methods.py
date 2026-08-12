Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> l = []
>>> l =[1,2,3.5,'str',True,[1,2,4],(1,2,3),{1,2,3},{1:1},3+8j]
>>> l
[1, 2, 3.5, 'str', True, [1, 2, 4], (1, 2, 3), {1, 2, 3}, {1: 1}, (3+8j)]
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a+b
[1, 2, 3, 4, 5, 6]
>>> a*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a = [123,45,67,43,4,6]
>>> a[0]
123
>>> a[1]
45
>>> a[-1]
6
>>> a[-2]
4
>>> a[:3]
[123, 45, 67]
>>> a[1:2]
[45]
>>> a[::2]
[123, 67, 4]
>>> a[-1:-4-1]
[]
>>> a[::-1]
[6, 4, 43, 67, 45, 123]
>>> a[:-3-1]
[123, 45]
>>> 45 in a
True
>>> 45 not in a
False
>>> min(a)
4
>>> max(a)
123
>>> sort(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    sort(a)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(a)
[4, 6, 43, 45, 67, 123]
len(a)
6
a
[123, 45, 67, 43, 4, 6]
id(a)
2162800324480
a[0] = 23
a
[23, 45, 67, 43, 4, 6]
id(a)
2162800324480
a.append(70)
a
[23, 45, 67, 43, 4, 6, 70]
a.insert(2,45)
a
[23, 45, 45, 67, 43, 4, 6, 70]
a.inser(1,55)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.inser(1,55)
AttributeError: 'list' object has no attribute 'inser'. Did you mean: 'insert'?
a.insert(1,55)

a
[23, 55, 45, 45, 67, 43, 4, 6, 70]
a.extend([1,3,5])
a
[23, 55, 45, 45, 67, 43, 4, 6, 70, 1, 3, 5]
a.pop()
5
a.pop()
3
a
[23, 55, 45, 45, 67, 43, 4, 6, 70, 1]
a.pop(0)
23
a
[55, 45, 45, 67, 43, 4, 6, 70, 1]
a.remove(67)
a
[55, 45, 45, 43, 4, 6, 70, 1]
a.remove(55)
a
[45, 45, 43, 4, 6, 70, 1]
del a[2]
a
[45, 45, 4, 6, 70, 1]
a.clear()
a
[]
id(a)
2162800324480
a = [12,33,45,66,78]
a.index(45)
2
a.count(12)
1
a.count(45)
1
a = [12,33,45,66,78]
a.sort()
a
[12, 33, 45, 66, 78]
1.sort()
SyntaxError: invalid decimal literal
1.sort()
SyntaxError: invalid decimal literal
a = [1,2,3,4]
b = a
b
[1, 2, 3, 4]
b.append(7)
b
[1, 2, 3, 4, 7]
a
[1, 2, 3, 4, 7]
anc = a.copy()
c.append(6)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    c.append(6)
NameError: name 'c' is not defined
c.append(12)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    c.append(12)
NameError: name 'c' is not defined
c = a.copy()
c
[1, 2, 3, 4, 7]
c.append(6)
c
[1, 2, 3, 4, 7, 6]
any([1,'',False,[],()])
True
any([0,'',False,[],()])
False
all([1,'',False,[],()])
False
a
[1, 2, 3, 4, 7]
sum(a)
17
7.sort()
SyntaxError: invalid decimal literal
a.sort()
a
[1, 2, 3, 4, 7]
a.reverse()
a
[7, 4, 3, 2, 1]
