Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> b=10.5
>>> c='vinith'
>>> print(a,b,c)
10 10.5 vinith
>>> print('a=',a,'b=',b,'c=',c)
a= 10 b= 10.5 c= vinith
>>> #Here we get gaps:so we use sep=''
>>> print('a=',a,'b=',b,'c=',c,sep='')
a=10b=10.5c=vinith
>>> KeyboardInterrupt
>>> print('a=',a,'b=',b,'c=',c,sep='\n')
a=
10
b=
10.5
c=
vinith
>>> KeyboardInterrupt
>>> print('a=',a,'b=',b,'c=',c,sep='\t')
a=	10	b=	10.5	c=	vinith
>>> print('a=',a,'b=',b,'c=',c,sep='\n\n')
a=

10

b=

10.5

c=

vinith
>>> #f string
>>> print(f'a={a} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={a} b={b} c={c}')
...       
a=10 b=10.5 c=vinith
>>> print(f'a={b} b={b} c={c})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f'a={b} b={b} c={c}')
...       
a=10.5 b=10.5 c=vinith
