# Practical 5: Implementing Linear and Binary Search Algorithms

## Objective
In this lab, you will implement both linear and binary search algorithms in Python. You'll learn about the differences between these search methods, their time complexities, and when to use each one. This exercise will help you practice algorithm implementation, list manipulation, and control structures in Python.

**Submission Date:** October 29th

## Prerequisites
- Basic knowledge of Python syntax
- Understanding of lists and functions in Python
- Familiarity with control structures (if statements, loops)

## Lab Steps

### Step 1: Implement Linear Search
Let's start by implementing the linear search algorithm:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")
```

### Step 2: Implement Binary Search
Now, let's implement the binary search algorithm. Remember, binary search requires a sorted list:

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Return the index if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Return -1 if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")
```

### Step 3: Implement Recursive Binary Search
Let's also implement a recursive version of binary search:

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the recursive function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")
```

### Step 4: Create a Main Function
Here's a complete program with a main function that demonstrates all search algorithms:

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def main():
    # Test data
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    test_list_sorted = sorted(test_list)
    
    print("Original list:", test_list)
    print("Sorted list:", test_list_sorted)
    print()
    
    # Test targets
    targets = [6, 5, 10]
    
    for target in targets:
        print(f"Searching for {target}:")
        
        # Linear search
        result_linear = linear_search(test_list, target)
        print(f"  Linear Search: Index = {result_linear}")
        
        # Binary search (iterative)
        result_binary = binary_search(test_list_sorted, target)
        print(f"  Binary Search: Index = {result_binary}")
        
        # Binary search (recursive)
        result_recursive = binary_search_recursive(test_list_sorted, target, 0, len(test_list_sorted) - 1)
        print(f"  Recursive Binary Search: Index = {result_recursive}")
        print()

if __name__ == "__main__":
    main()
```

## Expected Output
```
Original list: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
Sorted list: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

Searching for 6:
  Linear Search: Index = 7
  Binary Search: Index = 9
  Recursive Binary Search: Index = 9

Searching for 5:
  Linear Search: Index = 4
  Binary Search: Index = 6
  Recursive Binary Search: Index = 6

Searching for 10:
  Linear Search: Index = -1
  Binary Search: Index = -1
  Recursive Binary Search: Index = -1
```

## Key Differences Between Search Algorithms

| Algorithm | Time Complexity | Space Complexity | Requirements |
|-----------|----------------|------------------|--------------|
| Linear Search | O(n) | O(1) | No special requirements |
| Binary Search (Iterative) | O(log n) | O(1) | List must be sorted |
| Binary Search (Recursive) | O(log n) | O(log n) | List must be sorted |

## When to Use Each Algorithm
- **Linear Search**: Use when the list is small or unsorted
- **Binary Search**: Use when the list is large and sorted for better performance
- **Recursive Binary Search**: Use when you prefer a recursive approach, but be aware of stack limitations for very large lists