Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#health and fitness app data types of inputs
user_id=int(input())

=================================================== RESTART: C:/Users/Lenovo/OneDrive/Desktop/python-coursework/day- (6)/datatypes.py ==================================================
Inputs: 10482 72.5 Morning Run True
List Input: [120, 135, 142, 138, 150]
Set Input: {'calves', 'quads'}
Dict Input: {'unit': 'metric', 'mode': 'dark'}

Output Tuple: (True, 49.7, 'Morning Run', {'calves', 'quads'}, 'metric')
s= 'codeganan'
s
'codeganan'
type(s)
<class 'str'>
a =''
a
''
b='python'
c=' programming'
b+c
'python programming'
a*10
''
b*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
c**4
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c**4
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
pow(5).s
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pow(5).s
TypeError: pow() missing required argument 'exp' (pos 2)
"abc"*5
'abcabcabcabcabc'
# string accessing
c(4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    c(4)
TypeError: 'str' object is not callable
c[4]
'g'
c[-3]
'i'
c[0]
' '
c[1]
'p'
#slicing string
z = "vinith and vivek are learning programming"
z
'vinith and vivek are learning programming'
#z[intial index : ending index : charjump]
#z[intial index : ending index+1 : charjump]
z[0:5:1]
'vinit'
z[8:15:2]
'n ie'
z[8:15:1]
'nd vive'
z[21:26]
'learn'
#default is z[0:len(z):1]
#reverse a string
z[::-1]
'gnimmargorp gninrael era keviv dna htiniv'
  len(z)
  
SyntaxError: unexpected indent
len(z)
41
sorted(z)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'd', 'e', 'e', 'e', 'g', 'g', 'g', 'h', 'i', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'm', 'n', 'n', 'n', 'n', 'n', 'o', 'p', 'r', 'r', 'r', 'r', 't', 'v', 'v', 'v']
max(z)
'v'
min(z)
' '
ord("A")
65
#these are ascii values
ord('f')
102
ord("F")
70
chr(10)
'\n'
chr(70)
'F'
chr(99)
'c'
z.upper()
'VINITH AND VIVEK ARE LEARNING PROGRAMMING'
z.lower()
'vinith and vivek are learning programming'
z.capitalize()
'Vinith and vivek are learning programming'
z.swapcase()
'VINITH AND VIVEK ARE LEARNING PROGRAMMING'
z.swapcase()
'VINITH AND VIVEK ARE LEARNING PROGRAMMING'
z.casefold()
'vinith and vivek are learning programming'
z.centre()
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    z.centre()
AttributeError: 'str' object has no attribute 'centre'. Did you mean: 'center'?
z.center()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    z.center()
TypeError: center expected at least 1 argument, got 0
z.title()
'Vinith And Vivek Are Learning Programming'
z.center(50,"-")
'----vinith and vivek are learning programming-----'
z.center(51,"*")
'*****vinith and vivek are learning programming*****'
>>> z.ljust(50,"'")
"vinith and vivek are learning programming'''''''''"
>>> z.rjust(60,"-")
'-------------------vinith and vivek are learning programming'
>>> z.zfill(4)
'vinith and vivek are learning programming'
>>> z.zfill(90)
'0000000000000000000000000000000000000000000000000vinith and vivek are learning programming'
>>> s.zfill(30)
'000000000000000000000codeganan'
>>> z.zfill(10)
'vinith and vivek are learning programming'
>>> z.find('vinith')
0
>>> z.find('g')
28
>>> z.rfind('g')
40
>>> z.lfind('g')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    z.lfind('g')
AttributeError: 'str' object has no attribute 'lfind'. Did you mean: 'find'?
>>> z.find('x')
-1
>>> z.find('z')
-1
>>> z.count('a')
4
>>> z.count('g')
3
>>> z.replace('vivek','vicky')
'vinith and vicky are learning programming'
>>> z.replace('g','9')
'vinith and vivek are learnin9 pro9rammin9'
>>> s.maketrans("aeiou","!@#$!")
{97: 33, 101: 64, 105: 35, 111: 36, 117: 33}
>>> z.translate(s.maketrans("aeiou","!@#$!"))
'v#n#th !nd v#v@k !r@ l@!rn#ng pr$gr!mm#ng'
>>> z.encode()
b'vinith and vivek are learning programming'
>>> z.encode()
b'vinith and vivek are learning programming'
>>> b'vinith and vivek are learning programming'.decode()
'vinith and vivek are learning programming'
