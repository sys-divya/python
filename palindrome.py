import sys
print("start")
n=int(input("enter the no. of element:"))
if(n<=0):
    print("enter the valid no.")
    sys.exit(-1)
L=[]
while n>0:
    L.append(int(input("enter the element:")))
    n=n-1
print("List=",L)
i=0
f=0
j=n-1#1,2,2,1
while i<=n/2:
    
    if(L[i]==L[j]):
        i=i+1
        j=j-1
        f=1
    else:
        f=0
        break
    
if(f==1):
    print("no. is palindrome")
else:
    print("no. is not palindrome")




