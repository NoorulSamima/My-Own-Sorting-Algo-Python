# Sam Sort

**Sam Sort** is a custom sorting algorithm that works by repeatedly selecting the minimum element from an unsorted list and appending it to a new list. It is conceptually similar to Selection Sort but uses Python's built-in `min()` and `remove()` functions to simplify implementation.

---

## Algorithm Description

1. Initialize an empty result list.
2. While the input list is not empty:
   - Find the minimum element.
   - Append it to the result list.
   - Remove the minimum from the original list.
3. Return the result list.

---

This program stores the output in another array which makes it's time complexity to be O(n), if you find ways to store the output in the same array, feel free to contribute to the code

## Python Implementation

```python
def sam_sort(arr):
    i = 0
    res = []
    n = len(arr)
    while i <= (n - 1):
        res.append(min(arr))
        arr.remove(min(arr))
        i += 1
    return res

# Example
arr = [2.5, 9.2, 9.1, 5, 5.3, 4.9]
print(sam_sort(arr))  # Output: [2.5, 4.9, 5, 5.3, 9.1, 9.2]
