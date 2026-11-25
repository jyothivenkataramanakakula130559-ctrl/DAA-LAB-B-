def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


arr = list(map(int, input("Enter numbers separated by space: ").split()))
target = int(input("Enter number to search: "))

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
