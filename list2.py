l=[]
x=[]
v=[]
n=int(input("enter the no of ele.="))
if(n<=0):
    print("error not valid no.")
i=0
while(i<n):
    m=int(input("enter the ele.="))
    if(m%2==0):
        l.append(m)
        x.append(m**2)
        v.append(i)
    i=i+1

print(v,l,x)
