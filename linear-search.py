import array as ar
a=ar.array('i',[])
n=int(input("enter the limit of array\n"))
print("enter the array element")
for i in range(n):
    x=int(input())
    a.append(x)
s=int(input("enter the element for searching\n"))
f=0
for m in a:
    f=1
    break
if(f==1):
    print("searching success")
else:
    print("searching not success")
