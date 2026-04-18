from functions import *

def multi_table(n):
  ans=[]
  arr=[]
  for i in range(1,n+1):
    arr=[]
    for j in range(1,n+1):
      arr.append(i*j)
    ans.append(arr)
  return ans

if __name__ == '__main__':
    sizes=[100, 1000, 5000, 10000]
    for n in sizes:
        t = measure_time1(multi_table, n)

        print(f"{n:6d} | {t:10.6f}")