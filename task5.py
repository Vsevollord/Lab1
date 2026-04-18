from functions import *

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
   l_nums = [n for n in nums if n < q]

   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

if __name__ == '__main__':
    sizes=[100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time1(quicksort, arr)
        m = measure_memory(quicksort, arr)

        print(f"{n:6d} | {t:10.6f} | {m:12d} ")