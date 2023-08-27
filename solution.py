""" 
Assumptions/Design choices: 
- arrays are sorted into acending order
- each element can only be used in one pair
- return given as an int type
- lists only contain integers 
- becuase the array is in accending order a left and right pointer method can be used this
  makes the function more efficient than comparing each element to every other element
"""

def countingSumPairs(Array: list, X: int):
    # type validation of inputs
    if (type(X) != int):
        print("X input type error")
        return None
    if type(Array) != list:
        print("Array input type error")
        return None
        
    count = 0
    left = 0  # Pointer at the beginning of the array
    right = len(Array) - 1  # Pointer at the end of the array

    while left < right:
        current_sum = Array[left] + Array[right]
        if current_sum == X:
            count += 1
            left += 1  # Move the left pointer to the right
            right -= 1  # Move the right pointer to the left
        elif current_sum < X:
            left += 1  # move the left pointer to the right
        else:
            right -= 1  # Move the right pointer to the left

    return count

# Examples:
Array = [3,4,5,6]
X = 1
result = countingSumPairs(Array, X)
print(result)

Array = [0,15,32,2000,15000]
X = 15
result = countingSumPairs(Array, X)
print(result)

Array = [1,1,10,32,41]
X = 42
result = countingSumPairs(Array, X)
print(result)
