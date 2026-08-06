Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DataTypes
#1.Numeric data
#they are int ,float, complex
>>> a=12
>>> type(a)
<class 'int'>
3
>>> b=12.55
>>> type(b)
<class 'float'>
>>> c=2 +  10f
SyntaxError: invalid decimal literal
>>> c=2 + 10j
>>> print(c)
(2+10j)
>>> type(c)
<class 'complex'>
>>> #2.SEQUENCE DATA TYPES
>>> #They are string,list,tuple
>>> #String:
>>> hi="vinith"
>>> type(hi)
<class 'str'>
>>> #list:
>>> l1=[1,2,3,4,5]
>>> type(l1)
<class 'list'>
>>> #Tuple:
>>> dimensions = (10, 20, 30)
>>> type(dimensions)
<class 'tuple'>
>>> #Set types:
>>> #set:
>>> colors = {"Red", "Blue", "Green"}
>>> type(colors)
<class 'set'>
>>> #dictionary:
>>> student = {
... "name": "Rohit",
... "age": 21,
... "course": "Python"
... }
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
>>> student["name"]
'Rohit'
>>> type(student)
<class 'dict'>
#NONE SET:
Type=None
type(Type)
<class 'NoneType'>
