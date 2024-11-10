Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[True,10,3.12,'a']
l[0]
True
type(l[0])
<class 'bool'>
l[1]
10
type(l[1])
<class 'int'>
l[2]
3.12
type(l[2])
<class 'float'>
l=[[100,200,300],[400,500,600],[700,800,900]]
l
[[100, 200, 300], [400, 500, 600], [700, 800, 900]]
type[l]
type[[[100, 200, 300], [400, 500, 600], [700, 800, 900]]]
type(l)
<class 'list'>
l[0]
[100, 200, 300]
type(l[0])
<class 'list'>
len(l)
3
len(l[0])
3
l[0][0]
100
l[0][1]
200
l[0][2]
300
l[1][0]
400
l[1][1]
500
l[1][2]
600
l[2][0]
700
l[2][1]
800
l[2][2]
900
t=([True,10,['xyz','pl)
             
SyntaxError: unterminated string literal (detected at line 1)
t=([True,10,['xyz','pl']],600,True,{'a':[89,90],'b':(100,200)},{-23,-45})
             
t[0]
             
[True, 10, ['xyz', 'pl']]
t[1]
             
600
t[2]
             
True
t[3]
             
{'a': [89, 90], 'b': (100, 200)}
t[4]
             
{-23, -45}

type(t[0])
             
<class 'list'>
type(t[3])
             
<class 'dict'>
t[0][1]
             
10
t[0][0]
             
True
t[0][2]
             
['xyz', 'pl']
t[0][2][0]
             
'xyz'
t[0][2][1]
             
'pl'
t[0][2][1][0]
             
'p'
i=0
             
while i<len(t):
    print(t[i])
    i=i+1

    
[True, 10, ['xyz', 'pl']]
600
True
{'a': [89, 90], 'b': (100, 200)}
{-23, -45}
i=0
while i<len(t[0])
SyntaxError: expected ':'
while i<len(t[0]):
    print(t[0][i])
    i=i+1

    
True
10
['xyz', 'pl']
i=0
while i<len(t[0][2]):
    print(t[0][2][i])
    i=i+1

    
xyz
pl
i=0
while i<len(t[0][2][0]):
    print(t[0][2][0][i])
    i=i+1

    
x
y
z
i=0
t[3]
{'a': [89, 90], 'b': (100, 200)}
t[3]['a']
[89, 90]
t[3]['b']
(100, 200)
while i<len(t[3]['a']):
    print(t[3]['a'][i])
    i=i+1

    
89
90
l=[(['ab','xyzqzy',{(100,200):1000,'xyz':{350,605}},10,True],100,200),[114,34,118,14],'hello']
l[0]
(['ab', 'xyzqzy', {(100, 200): 1000, 'xyz': {605, 350}}, 10, True], 100, 200)
l[0][0]
['ab', 'xyzqzy', {(100, 200): 1000, 'xyz': {605, 350}}, 10, True]
l[0][1]
100
l[0][2]
200
l[0][3]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    l[0][3]
IndexError: tuple index out of range
l[0][0][0]
'ab'
l[0][0][0][0]
'a'
l[0][0][0][1]
'b'
l[0][0][1][0]
'x'
l[0][0][1][1]
'y'
l[0][0][1][2]
'z'
l[0][0][1][3]
'q'
l[0][0][1][4]
'z'
l[0][0][1][5]
'y'
l[0][0][1][6]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l[0][0][1][6]
IndexError: string index out of range
l[0][0][(100,200)]
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    l[0][0][(100,200)]
TypeError: list indices must be integers or slices, not tuple
l[0][0][2][(100,200)]
1000
l[0][0][2]['xyz']
{605, 350}
l[1]
[114, 34, 118, 14]
l[2]
'hello'
>>> l[2][0]
'h'
>>> l[2][1]
'e'
>>> l[2][2]
'l'
>>> l[2][3]
'l'
>>> i=0
>>> while i<len(l):
...     print(i,l[i])
...     i=i+1
... 
...     
0 (['ab', 'xyzqzy', {(100, 200): 1000, 'xyz': {605, 350}}, 10, True], 100, 200)
1 [114, 34, 118, 14]
2 hello
>>> #nested sequential container l[0]
>>> i=0
>>> while i<len(l[0]):
...     print(l[0][i])
...     i=i+1
... 
...     
['ab', 'xyzqzy', {(100, 200): 1000, 'xyz': {605, 350}}, 10, True]
100
200
>>> #nested-nested l[0][0]
>>> i=0
>>> while i<len(l[0][0])
SyntaxError: expected ':'
>>> :
...     
SyntaxError: invalid syntax
>>> i=0
... while i<len(l[0][0]):
...     
SyntaxError: multiple statements found while compiling a single statement
>>> j=0
>>> while j<len(l[0][0])
SyntaxError: expected ':'
>>> j=0
... while j<len(l[0][0]):
...     
SyntaxError: multiple statements found while compiling a single statement
