Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#input
a = input()
codegnan
a
'codegnan'
b = input()
1234
b
'1234'
c = input("enter : ")
enter : 12345
c
'12345'
cgpa= float(input())
122.12
cgpa
122.12
#split funnction
names.split()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    names.split()
NameError: name 'names' is not defined
names = input()
vivek vinith 
names.split()
['vivek', 'vinith']
names.split(',')
['vivek vinith ']
setinput = set(names.split())
setinput
{'vinith', 'vivek'}
tupleinput = tuple(names.split())
tupleinput
('vivek', 'vinith')
commagiven = input()
vivek,vinith
commagiven.split(',')
['vivek', 'vinith']
msrks = input().split()
12 34 76 64
marks
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    marks
NameError: name 'marks' is not defined. Did you mean: 'msrks'?
msrks
['12', '34', '76', '64']
map(int,msrks)
<map object at 0x000002AA6E4BD330>
list(map(int,msrks))
[12, 34, 76, 64]
tuple(map(int,msrks))
(12, 34, 76, 64)
set(map(int,msrks))
{64, 34, 12, 76}
s = 10
s
10
s='10'
s
'10'
int(int(s))
10
a,b = [1,2]
a
1
b
2
a,b,c = (1,1.5,'vinith')
a
1
b
1.5
c
'vinith'
name,marks  = input("enter name and pw : ").split()
enter name and pw : vivek 100
name
'vivek'
marks
'100'
int(marks)
100
