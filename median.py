import statistics
a=list()
nu=input()
for i in range(int(nu)):
  n=input()
  a.append(int(n))
print(a)
a.sort()
print(a)
print(statistics.median(a))
