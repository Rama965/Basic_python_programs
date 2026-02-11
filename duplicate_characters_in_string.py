s1 = "Programming"
duplicates = set()
for ch in s1:
    if s1.count(ch)>1:
        duplicates.add(ch)
print(duplicates)