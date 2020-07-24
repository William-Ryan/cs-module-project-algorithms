'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    
    window_arr = []
    array_output = []
    while 0 < len(nums) - (k-1):
        for number in nums[0:k]:
            window_arr.append(number)
        window_arr.sort()
        max_number = window_arr[k-1]
        array_output.append(max_number)
        nums.pop(0)
        window_arr = []
    return array_output

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
