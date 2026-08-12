Python 3.14.5 (tags/v3.14.5:5607950, May 10 2026, 10:43:50) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = '   Hello    world     "
SyntaxError: unterminated string literal (detected at line 1)
s = '      Hello    world   '
s.strip()
'Hello    world'
s.lstrip()
'Hello    world   '
s.rstrip()
'      Hello    world'
s.replace(' ','')
'Helloworld'
s = 'python-java-sql-Html'
s.split('-')
['python', 'java', 'sql', 'Html']
s.split('-',2)
['python', 'java', 'sql-Html']
s.rsplit('-',2)
['python-java', 'sql', 'Html']
l = '''python'''
l ='''python
java
mysql
flask
'''
l
'python\njava\nmysql\nflask\n'
l.splitlines()
['python', 'java', 'mysql', 'flask']
c = ['python', 'java', 'mysql', 'flask']
c
['python', 'java', 'mysql', 'flask']
''.join
<built-in method join of str object at 0x00007FFBEE921790>
''.join(c)
'pythonjavamysqlflask'
' '.join(c)
'python java mysql flask'
'@'.join(c)
'python@java@mysql@flask'
a = 'strings.py'
a.partition('.')
('strings', '.', 'py')
a = 'string.py.java.sql.txt'
a.rpartition()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a.rpartition()
TypeError: str.rpartition() takes exactly one argument (0 given)
a.rpartition('.')
('string.py.java.sql', '.', 'txt')
a.partition('.')
('string', '.', 'py.java.sql.txt')
>>> a ='strings.png'
>>> a.startswith('string')
True
>>> a.endswith('.py')
False
>>> a.endswith('.png')
True
>>> 'pyhton.13'.islower()
True
>>> 'PYTHON.13@#$%.isupper()
SyntaxError: unterminated string literal (detected at line 1)
>>> 'PYTHON.13@#$%'.isupper()
True
>>> 'estyu'.isalpha()
True
>>> 'estur@#'.isalpha()
False
>>> 'estyu@2345'.isalnum()
False
>>> '23456'.isalnum()
True
>>> '  '.isspace()
True
>>> '   Hello'.isspace()
False
>>> 'HLO Wor'.istitle()
False
>>> 'Hlo Word'istitle()
SyntaxError: invalid syntax
>>> 'Hlo Word'.istitle()
True
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> '1234'.isdecimal()
True
>>> 'sdseeff'.isdecimal()
False
>>> '8756'.isnumeric()
True
