from functions import *

def second_max(a):
  max1=max2=a[0]
  for i in a:
    if i>max1:
      max2=max1
      max1=i

  return max2

if __name__ == '__main__':
    sizes=[100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time1(second_max, arr)

        print(f"{n:6d} | {t:10.6f}")