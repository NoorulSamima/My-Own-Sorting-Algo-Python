from sam_sort.sam_sort import sam_sort

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ")
        arr = list(map(float, user_input.strip().split()))
        sorted_arr = sam_sort(arr)
        print("Sorted array:", sorted_arr)
    except ValueError:
        print("Please enter valid numbers.")