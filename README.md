# Лабораторная работа 1
## Выполнил: Прудкин Всеволод ИДБ-25-02

### Вспомогательные Функции
1. Функция измерения памяти
```python
def measure_memory(func, data):
    tracemalloc.start()
    tracemalloc.clear_traces()
    result = func(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak
```
2. Функции измерения времени
```python
def measure_time1(func, data): # Для функции с 1 аргументом
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return float(end - start)

def measure_time2(func, data1,data2): # Для функции с 2 аргументами
    start = time.perf_counter()
    func(data1,data2)
    end = time.perf_counter()
    return float(end - start)
```
3. Функция генерации случайного массива
```python
def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100000))
    return arr
```

### 1. Проверка наличия элемента в массиве

1. Реализация

```python
def find_in_array(a,n):
  for i in a:
    if i==n:
      return True
  return False
```

2. Результат
```python
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
```
| n | t,с |
|---|---|
| 100 | 0.000003 |
| 1000 | 0.000018 |
| 5000 | 0.000220 |
| 10000 | 0.000421 |


### 2. Поиск второго максимального элемента
Алгоритм должен найти второе по величине число в массиве.
1. Реализация

```python
def second_max(a):
  max1=max2=a[0]
  for i in a:
    if i>max1:
      max2=max1
      max1=i
```

2. Результат
```python
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
```
| n | t,с |
|---|---|
| 100 | 0.000008 |
| 1000 | 0.000042 |
| 5000 | 0.000201 |
| 10000 | 0.000414 |

### 3. Бинарный поиск
Бинарный поиск используется для поиска элемента в **отсортированном массиве**.

1. Реализация

```python
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
```

2. Результат
```python
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
        arr = sorted(generate_array(i))
        n = random.randint(0, 100000)
        t = measure_time2(bin_search, arr,n)

        print(f"{i:6d} | {t:10.6f}")
```
| n | t,с |
|---|---|
| 100 | 0.000003 |
| 1000 | 0.000004 |
| 5000 | 0.000005 |
| 10000 | 0.000005 |

### 4. Построение таблицы умножения
1. Реализация

```python
def multi_table(n):
  ans=[]
  arr=[]
  for i in range(1,n+1):
    arr=[]
    for j in range(1,n+1):
      arr.append(i*j)
    ans.append(arr)
  return ans
```

2. Результат
```python
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
```
| n | t,с |
|---|---|
| 100 | 0.001129 |
| 1000 | 0.108380 |
| 5000 | 2.662635 |
| 10000 | 11.494340 |

## Провести замеры алгоритмической и пространственной сложности любой из сортировок
1. Результат
```python
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
```
| n | t,с | m,байт|
|---|---|---|
| 100 | 0.000116 | 3048 |
| 1000 | 0.001461 | 44184 |
| 5000 | 0.014586 | 155672 |
| 10000 | 0.032304 | 588664 |
