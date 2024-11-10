s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="abcdefghijklmnopqrstuvwxyz"
s3="012345678"
#s4="~!@#$%^&*()_=+-{}[]:;<>,./?|\"
print("ASCII code for capital leter")
for c in s1:
    print("ascii({})".format(c), ord(c),sep="=")
print("ASCII code for small leter")
for c in s2:
    print("ascii({})".format(c), ord(c),sep="=")
print("ASCII code for no. leter")
for c in s3:
    print("ascii({})".format(c), ord(c),sep="=")
#print("ASCII code for sym leter")
#for cin s4:
 #   print("ascii({})".format(c), ord(c),sep="=")




