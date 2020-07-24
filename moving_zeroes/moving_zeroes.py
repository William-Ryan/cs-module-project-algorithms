'''
Input: a List of integers
Returns: a List of integers
'''
def naive_moving_zeroes(arr):
    holder = []

    for num in arr:
        if num == 0:
            holder.append(num)
        else:
            holder.insert(0, num)

    return holder

def moving_zeroes(arr):
    count = 0

    for index in range(len(arr)):
        if arr[index] != 0:
            arr[count] = arr[index]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")