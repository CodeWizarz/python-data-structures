# arrays_examples.py

# Example: Finding the maximum element in an array

def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

# Test the function
test_array = [1, 20, 3, 4, 5, 6]
print("Maximum value:", find_max(test_array))  # Output: Maximum value: 20