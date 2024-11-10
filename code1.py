import sys
n=int(input("no. of ele:"))
if(n<=0):
    sys.exit(-1)
L=[]
Ln=[]
Le=[]
Lpr=[]
i=0
while i<n:
    L.append(int (input("no.:")))
    i=i+1
print(L)
j=2
k=0
for i in L:
    if(i<0):
        Ln.append(i)
    if (i%2==0):
        Le.append(i)
    
    while k<n:
        if(n%j==0):
            break
        k=k+1
    if(k==n):
        Lpr.append(n)
print(Ln)
print(Le)
print(Lpr)
        
    
    
