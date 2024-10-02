def counting_sort(arr):
    max_value = max(arr)
    count_arr = [0] * (max_value + 1)

    for num in arr:
        count_arr[num] += 1

    for i in range(1, max_value + 1):
        count_arr[i] += count_arr[i - 1]

    sorted_arr = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1

    return sorted_arr

if __name__ == "__main__":
    user_input = list(map(int, input("Enter numbers separated by spaces: ").split()))
    sorted_output = counting_sort(user_input)
    
    print("Sorted array:")
    for num in sorted_output:
        print(num, end=" ")
