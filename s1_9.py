m=int(input())
if(m<1 or (m%1)!=0):
print("wrong input")
else:
temp=0
while(m!=0):
temp=temp+n
m=m-1
print(temp)
