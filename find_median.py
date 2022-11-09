def findMedian():
    n = int(input().strip())
    arr = sorted(list(map(int, input().rstrip().split())))
    print(arr)
    half = int((n+1)/2)
    result = [arr[-half]]
    print(str(result[0]) + '\n')

findMedian()






