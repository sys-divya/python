Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#tuple datatype
t=()
t=(10,20,30,40,50,60,70,80,90,100)
for x in t:
    print(x)

    
10
20
30
40
50
60
70
80
90
100
t=(10)
type(t)
<class 'int'>
t=(10,)
type(t)
<class 'tuple'>
w="ankush"
t=tuple(w)
t
('a', 'n', 'k', 'u', 's', 'h')
d={'a':10,'b':34}
t1=tuple(d.keys())
t1
('a', 'b')
t2=tuple(d.items())
t2
(('a', 10), ('b', 34))
s={"ankush",True,10}
t3=tuple(s)
t3
(True, 10, 'ankush')
#builtin function
#operators
t=(10,20,30,40,50,60,70,80,90,100)
for x in range(len(t)):
    print(x,t[x])

    
0 10
1 20
2 30
3 40
4 50
5 60
6 70
7 80
8 90
9 100
>>> t[1:5]
(20, 30, 40, 50)
>>> t[::-1]
(100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
>>> t2=(100,200,300)
>>> t3=t+t2
>>> t3
(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 200, 300)
>>> t3*3
(10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 200, 300, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 200, 300, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 200, 300)
>>> -10 not in t
True
>>> t3.count()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t3.count()
TypeError: tuple.count() takes exactly one argument (0 given)
>>> t3.count(10)
1
>>> t3.index(10,4)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t3.index(10,4)
ValueError: tuple.index(x): x not in tuple
>>> t3.index(10)
0
>>> dir tuple
SyntaxError: invalid syntax
>>> dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
