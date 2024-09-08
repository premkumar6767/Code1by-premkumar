def findTwoDistinct(arr):
    xor = 0
    num1 = 0
    num2 = 0

    # XOR of all elements
    for num in arr:
        xor ^= num

    # Find the rightmost set bit in xor
    set_bit = xor & ~(xor - 1)

    # Divide elements into two groups and XOR them separately
    for num in arr:
        if num & set_bit:
            num1 ^= num  # Group with set_bit set
        else:
            num2 ^= num  # Group with set_bit not set

    # Return the result in increasing order
    return sorted([num1, num2])

# Input
N = int(input("Enter the value of N: "))
arr = list(map(int, input(f"Enter {2 * N + 2} elements: ").split()))

# Find and print the two distinct numbers
result = findTwoDistinct(arr)
print(result[0], result[1])