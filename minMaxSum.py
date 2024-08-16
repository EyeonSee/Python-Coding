def miniMaxSum(arr):
    arr = list(map(int, arr.strip().split()))
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[-4:])
    print(min_sum, max_sum)

arr = input()
miniMaxSum(arr)