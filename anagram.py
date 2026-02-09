a = input()
b = input()
if sorted(a.lower()) == sorted(b.lower()):
    print("Anagram")
else:
    print("Not a Anagram")