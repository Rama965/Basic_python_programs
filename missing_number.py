n = int(input("Enter total numbers: "))
lst = list(map(int,input().split()))
missing = n*(n+1)//2 - sum(lst)
print(missing)