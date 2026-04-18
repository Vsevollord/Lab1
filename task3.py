from functions import *

def bin_search(a, n):
    left = 0
    right = len(a) - 1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == n:
            return mid

        if a[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    sizes=[100, 1000, 5000, 10000]
    for i in sizes:
        arr = generate_array(i)
        n = random.randint(0, 100)
        t = measure_time2(bin_search, arr,n)

        print(f"{i:6d} | {t:10.6f}")