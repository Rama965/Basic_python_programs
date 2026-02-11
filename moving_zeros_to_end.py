lst = [0,3,4,0,3,0,1]
#list compheresion -- A list comprehension in Python provides a concise and efficient way to create a new list based on an existing iterable (like a list, tuple, or range) in a single line of code.
res = [i for i in lst if i!=0]+[0]*lst.count(0)
print(res)