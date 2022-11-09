
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    right = 0
    left = 0
    i = 0
    j = -1
    arrlen = len(arr)

    # for i in range(n):           # for a loop use this line and line 20,
    while i < arrlen:              # and remove this line.
        right += arr[i][i]
        left += arr[i][0 - 1 - i]
        i += 1
        # j -= 1
    return abs(right - left)


