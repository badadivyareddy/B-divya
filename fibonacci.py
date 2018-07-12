def fibo_recur(x):
if x<=1:
return x
else:
return(fibo_recur(x-1)+fibo_recur(x-2))
n=int(input())
if n<=0:
print()
else:
for i in range(n):
print(fibo_recur(i))
