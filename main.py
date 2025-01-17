def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0 
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Worst-case steps: {steps}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(f"Worst-case steps: {steps}")
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter the list of numbers (comma-separated): ").split(',')))
    target = int(input("Enter the number to search: "))

    print("\nUsing Linear Search:")
    result = linear_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
    
    print("\nUsing Binary Search:")
    arr.sort()
    print(f"Sorted array: {arr}")
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")
