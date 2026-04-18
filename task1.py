from functions import *

def find_in_array(a,n):
  for i in a:
    if i==n:
      return True
  return False

if __name__ == '__main__':
    sizes=[100, 1000, 5000, 10000]
    for i in sizes:
        arr = generate_array(i)
        n = random.randint(0, 100)
        t = measure_time2(find_in_array, arr,n)

        print(f"{i:6d} | {t:10.6f}")