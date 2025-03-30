n=int(input("Enter n :"))
res=n
for i in range(n,1,-1):
    res=res*(n-1)
    n=n-1
print(res)