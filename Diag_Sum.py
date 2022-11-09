
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    d = (arr[0][0] + arr[1][1] + arr[2][2]) - (arr[0][2] + arr[1][1] + arr[2][0])
    return abs(d)


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)

print(str(result))