lst = list(map(int,input("Enter numbers you want to sum: ").split()))
def sum_of_list(lst):
    sum = 0
    for num in range(len(lst)):
        sum += lst[num]
    return sum
print(sum_of_list(lst))
