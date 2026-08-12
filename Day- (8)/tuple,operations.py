Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t=()
t=(1,2,3,45)
t
(1, 2, 3, 45)
t()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    t()
TypeError: 'tuple' object is not callable
type(t).
SyntaxError: invalid syntax
type(t)
<class 'tuple'>
t=(1.22.5,[1,2,3,4],{1,2,3,4},{1:1,2:3},True,"str")
SyntaxError: invalid syntax. Perhaps you forgot a comma?
t=(1,22.5,[1,2,3,4],{1,2,3,4},{1:1,2:3},True,"str")
t
(1, 22.5, [1, 2, 3, 4], {1, 2, 3, 4}, {1: 1, 2: 3}, True, 'str')
type(t)
<class 'tuple'>
#Concatination:
(1,2,3)+(2,3,4)
(1, 2, 3, 2, 3, 4)
t=(1,22.5,[1,2,3,4],{1,2,3,4},{1:1,2:3},True,"str")
t[1]
22.5
t[::-1]
('str', True, {1: 1, 2: 3}, {1, 2, 3, 4}, [1, 2, 3, 4], 22.5, 1)
(1,2,3)*4
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
t
(1, 22.5, [1, 2, 3, 4], {1, 2, 3, 4}, {1: 1, 2: 3}, True, 'str')
t[2:4]
([1, 2, 3, 4], {1, 2, 3, 4})
t[-1:-3:-1].
SyntaxError: invalid syntax
t[-1:-4:-1]
('str', True, {1: 1, 2: 3})
>>> 'str' in t
True
>>> 22.5 in t
True
>>> False in t
False
>>> t=(12,789,32,13)
>>> sorted(t)
[12, 13, 32, 789]
>>> max(t)
789
>>> min(t)
12
>>> len(t)
4
>>> t.count(32)
1
>>> t.index(32)
2
>>> all(1,2,5)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    all(1,2,5)
TypeError: all() takes exactly one argument (3 given)
>>> all((1,2,5))
True
>>> any(0,1,2)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    any(0,1,2)
TypeError: any() takes exactly one argument (3 given)
>>> any((0,1,2))
True
>>> t
(12, 789, 32, 13)
>>> sum(t)
846
>>> t[3]
13
>>> t=(1, 22.5, [1, 2, 3, 4], {1, 2, 3, 4}, {1: 1, 2: 3}, True, 'str')
>>> t[3]
{1, 2, 3, 4}
>>> t[:3]
(1, 22.5, [1, 2, 3, 4])
>>> t[1:8]
(22.5, [1, 2, 3, 4], {1, 2, 3, 4}, {1: 1, 2: 3}, True, 'str')
