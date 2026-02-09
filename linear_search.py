lst = list(map(int,input("Enter numbers: ").split()))
target = int(input("Enter element to found: "))

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element found at {i}th index"
    return f"Element Not Found"
print(linear_search(lst))