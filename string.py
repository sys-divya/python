Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=8994
del n
print(n)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(n)
NameError: name 'n' is not defined
s1="divya"
s2='divya'
print(type(s1),type(s))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(type(s1),type(s))
NameError: name 's' is not defined. Did you mean: 's1'?
print(type(s1),type(s2))
<class 'str'> <class 'str'>
s3="my name is divya"
s4='my name is "diya"'
s4
'my name is "diya"'
s3="my name is 'divya'"
s3
"my name is 'divya'"
print(s3)
my name is 'divya'

============================= RESTART: D:/python/myprg1.py =============================
ASCII code for capital leter
ascii(A)=65
ascii(B)=66
ascii(C)=67
ascii(D)=68
ascii(E)=69
ascii(F)=70
ascii(G)=71
ascii(H)=72
ascii(I)=73
ascii(J)=74
ascii(K)=75
ascii(L)=76
ascii(M)=77
ascii(N)=78
ascii(O)=79
ascii(P)=80
ascii(Q)=81
ascii(R)=82
ascii(S)=83
ascii(T)=84
ascii(U)=85
ascii(V)=86
ascii(W)=87
ascii(X)=88
ascii(Y)=89
ascii(Z)=90
ASCII code for small leter
ascii(a)=97
ascii(b)=98
ascii(c)=99
ascii(d)=100
ascii(e)=101
ascii(f)=102
ascii(g)=103
ascii(h)=104
ascii(i)=105
ascii(j)=106
ascii(k)=107
ascii(l)=108
ascii(m)=109
ascii(n)=110
ascii(o)=111
ascii(p)=112
ascii(q)=113
ascii(r)=114
ascii(s)=115
ascii(t)=116
ascii(u)=117
ascii(v)=118
ascii(w)=119
ascii(x)=120
ascii(y)=121
ascii(z)=122
ASCII code for no. leter
ascii(0)=48
ascii(1)=49
ascii(2)=50
ascii(3)=51
ascii(4)=52
ascii(5)=53
ascii(6)=54
ascii(7)=55
ascii(8)=56

============================= RESTART: D:/python/myprg1.py =============================
ASCII code for capital leter
ascii(A)=65
ascii(B)=66
ascii(C)=67
ascii(D)=68
ascii(E)=69
ascii(F)=70
ascii(G)=71
ascii(H)=72
ascii(I)=73
ascii(J)=74
ascii(K)=75
ascii(L)=76
ascii(M)=77
ascii(N)=78
ascii(O)=79
ascii(P)=80
ascii(Q)=81
ascii(R)=82
ascii(S)=83
ascii(T)=84
ascii(U)=85
ascii(V)=86
ascii(W)=87
ascii(X)=88
ascii(Y)=89
ascii(Z)=90
ASCII code for small leter
ascii(a)=97
ascii(b)=98
ascii(c)=99
ascii(d)=100
ascii(e)=101
ascii(f)=102
ascii(g)=103
ascii(h)=104
ascii(i)=105
ascii(j)=106
ascii(k)=107
ascii(l)=108
ascii(m)=109
ascii(n)=110
ascii(o)=111
ascii(p)=112
ascii(q)=113
ascii(r)=114
ascii(s)=115
ascii(t)=116
ascii(u)=117
ascii(v)=118
ascii(w)=119
ascii(x)=120
ascii(y)=121
ascii(z)=122
ASCII code for no. leter
ascii(0)=48
ascii(1)=49
ascii(2)=50
ascii(3)=51
ascii(4)=52
ascii(5)=53
ascii(6)=54
ascii(7)=55
ascii(8)=56

============================== RESTART: D:/python/ascii.py =============================
ASCII code for capital leter
ascii(A)=65
ascii(B)=66
ascii(C)=67
ascii(D)=68
ascii(E)=69
ascii(F)=70
ascii(G)=71
ascii(H)=72
ascii(I)=73
ascii(J)=74
ascii(K)=75
ascii(L)=76
ascii(M)=77
ascii(N)=78
ascii(O)=79
ascii(P)=80
ascii(Q)=81
ascii(R)=82
ascii(S)=83
ascii(T)=84
ascii(U)=85
ascii(V)=86
ascii(W)=87
ascii(X)=88
ascii(Y)=89
ascii(Z)=90
ASCII code for small leter
ascii(a)=97
ascii(b)=98
ascii(c)=99
ascii(d)=100
ascii(e)=101
ascii(f)=102
ascii(g)=103
ascii(h)=104
ascii(i)=105
ascii(j)=106
ascii(k)=107
ascii(l)=108
ascii(m)=109
ascii(n)=110
ascii(o)=111
ascii(p)=112
ascii(q)=113
ascii(r)=114
ascii(s)=115
ascii(t)=116
ascii(u)=117
ascii(v)=118
ascii(w)=119
ascii(x)=120
ascii(y)=121
ascii(z)=122
ASCII code for no. leter
ascii(0)=48
ascii(1)=49
ascii(2)=50
ascii(3)=51
ascii(4)=52
ascii(5)=53
ascii(6)=54
ascii(7)=55
ascii(8)=56
n=523
bin(523)
'0b1000001011'
s="523"
bin(n)[2:]
'1000001011'
for c in s:
    print("({})".format(c),ord(c),sep="=")
... 
...     
(5)=53
(2)=50
(3)=51
>>> for c in s:
...     print(bin(ord(c))[2:])
... 
...     
110101
110010
110011
>>> type(n)
<class 'int'>
>>> s=n
>>> type(s)
<class 'int'>
>>> n=int(40)
>>> n
40
>>> m=int()
>>> m
0
>>> s=str(n)
>>> type
<class 'type'>
>>> type(s)
<class 'str'>
>>> #type converstion
>>> s="78"
>>> n=int(s)
>>> print (type(n))
<class 'int'>
>>> print(n+2,n-2,n**2)
80 76 6084
>>> print(s+s)
7878
>>> n=input
>>> n=input("n=")
n=45
>>> type(n)
<class 'str'>
>>> n=int(input("n="))
n=56
>>> type(n)
<class 'int'>
