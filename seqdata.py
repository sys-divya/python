Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=["ss"]
e=enumerate(l)
type(e)
<class 'enumerate'>
print(e)
<enumerate object at 0x0000022B11A4DAD0>
for i in e
SyntaxError: expected ':'
for i in e:
    print(i)

    
(0, 'ss')
a,b=9,8
a,b
(9, 8)
for (ind,val) in e:
    print(ind,val)

    


d={"a":10,"b":30,"c":50}
d.keys()
dict_keys(['a', 'b', 'c'])
d.items()
dict_items([('a', 10), ('b', 30), ('c', 50)])
for (key,val) in d.items():
    print(key,val)

    
a 10
b 30
c 50
for (key,val) in d.items():
    print(key,val*2)

    
a 20
b 60
c 100
for (ind,val) in enumerate(l):
    print(ind,val)

    
0 ss
s={10,20,30,40}
for i in range(len(s)):
    print(i)

    
0
1
2
3
for i in range(len(s)):
    print(i,s[i])

    
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    print(i,s[i])
TypeError: 'set' object is not subscriptable
'set' object is not subscriptable
for (
    
SyntaxError: invalid syntax

for (i,v) in enumerate(s):
    print(i,v)

0 40
1 10
2 20
3 30
g="shrirampur"
for(i,v) in enumerate(g):
    print(g)

shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
shrirampur
for(i,v) in enumerate(g):
    print(i,v)

0 s
1 h
2 r
3 i
4 r
5 a
6 m
7 p
8 u
9 r
9 r
SyntaxError: invalid syntax
d={"a":2222,"b":232,"c":333}
for(i,v) in enumerate(d):
    print(i,v)

0 a
1 b
2 c
>>> t=(2,3,5,6)
>>> for(i,v) in enumerate(t):
... 
... 
...     print(i,v)
... 
0 2
1 3
2 5
3 6
>>> l=[10,20,30,40,50,60]
>>> for i in l:
...     print(i)
... 
10
20
30
40
50
60
>>> for (i ,v ) in enumerate(l):
...     print(i,l[i])
... 
0 10
1 20
2 30
3 40
4 50
5 60
>>> for i in range(len(i)):
...     print(i,l[i])
... 
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    for i in range(len(i)):
TypeError: object of type 'int' has no len()
>>> for i in range(len(l)):
...     print(i,l[i])
... 
0 10
1 20
2 30
3 40
4 50
5 60
