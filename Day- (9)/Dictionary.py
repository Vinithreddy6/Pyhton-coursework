Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dict: It is mutable  ,ord,hetro ,dyn
d={}
type(d)
<class 'dict'>
d={1:4,2:4,3:5}
d
{1: 4, 2: 4, 3: 5}
d={}
d[1]=1
d[12.3]=1
d['str']=1
d[(1,2,4)]=1
d[(2+3j)]=1
d[True]=1
d[[1,2,3]]=1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    d[[1,2,3]]=1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
del d[1]

d
{12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1}
d[1]=1
d[2]=12.3
d[3]='str'
d[4]=2+3j
d[5]=True
d[6]=(1,2,3)
d
{12.3: 1, 'str': 1, (1, 2, 4): 1, (2+3j): 1, 1: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: (1, 2, 3)}
data={'name:vinith','course:pfs','batch"65'}
data
{'batch"65', 'name:vinith', 'course:pfs'}
data={'name:vinith','course:pfs','batch:65'}
data
{'name:vinith', 'course:pfs', 'batch:65'}
name in data
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name in data
NameError: name 'name' is not defined
'vinith' in data
False
'name' in data
False
data={'name':'vinith','course':'pfs','batch':'65'}
data
{'name': 'vinith', 'course': 'pfs', 'batch': '65'}
'name' in data
True
'vinith' in data
False
'course' in data
True
'pfs' in data
False
data['name']
'vinith'
data['age']
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    data['age']
KeyError: 'age'
data['batch']
'65'
data.get['age']
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    data.get['age']
TypeError: 'builtin_function_or_method' object is not subscriptable
data.get('age')
data.get('key')
data.get('batch','key is present')
'65'
data.update('age':'22')
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
data.update({'age':'22'})
data
{'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22'}
data.update({'email: v@gamil.com','phn:123})
             
SyntaxError: unterminated string literal (detected at line 1)
data.update({'email: v@gamil.com','phn:123'})
             
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data.update({'email: v@gamil.com','phn:123'})
ValueError: dictionary update sequence element #0 has length 7; 2 is required
data
             
{'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22'}
data.update({'email: v@gamil.com','phn:123'})
             
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    data.update({'email: v@gamil.com','phn:123'})
ValueError: dictionary update sequence element #0 has length 7; 2 is required
data.update({'email':' v@gamil.com','phn':'123'})
             
data
             
{'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22', 'email': ' v@gamil.com', 'phn': '123'}
data.popitem()
             
('phn', '123')
data.popitem()

('email', ' v@gamil.com')
data.remove('name')
             
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    data.remove('name')
AttributeError: 'dict' object has no attribute 'remove'
data.clear()
             
data
             
{}
data={'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22'}
             
len(data)
             
4
data.keys()
             
dict_keys(['name', 'course', 'batch', 'age'])
data.values()
             
dict_values(['vinith', 'pfs', '65', '22'])
max(data)
             
'name'
min(data)
             
'age'
>>> d={1:1,2:2}
...              
>>> d
...              
{1: 1, 2: 2}
>>> m=d
...              
>>> m
...              
{1: 1, 2: 2}
>>> m[3]=5
...              
>>> d
...              
{1: 1, 2: 2, 3: 5}
>>> m
...              
{1: 1, 2: 2, 3: 5}
>>> n=d.copy()
...              
>>> n[5]=9
...              
>>> n=
...              
SyntaxError: invalid syntax
>>> n
...              
{1: 1, 2: 2, 3: 5, 5: 9}
>>> d
...              
{1: 1, 2: 2, 3: 5}
>>> data
...              
{'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22'}
>>> data.get('age')
...              
'22'
>>> data.setdefault('key',2)
...              
2
>>> data
...              
{'name': 'vinith', 'course': 'pfs', 'batch': '65', 'age': '22', 'key': 2}
>>> data.items()
...              
dict_items([('name', 'vinith'), ('course', 'pfs'), ('batch', '65'), ('age', '22'), ('key', 2)])
