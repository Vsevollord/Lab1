import time
import random
import tracemalloc


def measure_memory(func, data):
    tracemalloc.start()
    tracemalloc.clear_traces()
    result = func(data)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak

def measure_time1(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return float(end - start)

def measure_time2(func, data1,data2):
    start = time.perf_counter()
    func(data1,data2)
    end = time.perf_counter()
    return float(end - start)

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 100000))
    return arr

def print_matrrix(matrix):
  for row in matrix:
      for element in row:
          print(f"{element:3d}", end=' ')
      print()


