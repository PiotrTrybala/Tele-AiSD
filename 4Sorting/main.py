
import numpy as np
import time
from tqdm import tqdm

def insertion_soft(A):
    for i in range(1, len(A) - 1):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j + 1] = A[j]
            j = j - 1
        A[j+1] = x

def merge_sort(A, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort(A, l, m)
        merge_sort(A, m + 1, r)
        merge(A, l, r, m)

def merge(A, l, r, m):

    l1 = m - l + 1
    l2 = r - m

    L = [0] * l1
    R = [0] * l2

    for i in range(l1):
        L[i] = A[l + i]
    for i in range(l2):
        R[i] = A[m + 1 + i]

    i = j = 0
    k = l
    while i < l1 and j < l2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < l1:
        A[k] = L[i]
        i += 1
        k += 1

    while j < l2:
        A[k] = R[j]
        j += 1
        k += 1

# np.random.seed(42)

def get_random_array(n):
    return np.random.randint(0, 1000, size=n).tolist()


INSERTION_SORT_TIMES = {}
MERGE_SORT_TIMES = {}
ARRAY_LENGTH = 2 * 10**3

# insertion sort

for n in tqdm(range(ARRAY_LENGTH)):
    s = time.time()
    insertion_soft(get_random_array(n))
    e = time.time() - s
    INSERTION_SORT_TIMES[n] = e

# merge sort

for n in tqdm(range(ARRAY_LENGTH)):
    s = time.time()
    arr = get_random_array(n)
    merge_sort(arr, 0, len(arr) - 1)
    e = time.time() - s
    MERGE_SORT_TIMES[n] = e

print("Results:")
print(f"Insertion soft: Lowest: {INSERTION_SORT_TIMES[min(INSERTION_SORT_TIMES, key=INSERTION_SORT_TIMES.get)]:.5f}s, Highest: {INSERTION_SORT_TIMES[max(INSERTION_SORT_TIMES, key=INSERTION_SORT_TIMES.get)]:.5f}s, Mean: {np.mean(list(INSERTION_SORT_TIMES.values())):.5f}s")
print(f"Merge soft: Lowest: {MERGE_SORT_TIMES[min(MERGE_SORT_TIMES, key=MERGE_SORT_TIMES.get)]:.5f}s, Highest: {MERGE_SORT_TIMES[max(MERGE_SORT_TIMES, key=MERGE_SORT_TIMES.get)]:.5f}s, Mean: {np.mean(list(MERGE_SORT_TIMES.values())):.5f}s")

import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker

x_a, y_a = zip(*sorted(INSERTION_SORT_TIMES.items()))
x_b, y_b = zip(*sorted(MERGE_SORT_TIMES.items()))

plt.figure(figsize=(8, 5))
plt.scatter(x_a, y_a, label="Insertion sort", marker='o')
plt.scatter(x_b, y_b, label="Merge sort", marker='x')

plt.xlabel('Array size')
plt.ylabel('Execution time (s)')

plt.legend()
plt.grid(True, which='both', ls='--', linewidth=0.5)

plt.title('Insertion sort vs Merge sort - Execution times')
plt.tight_layout()
plt.savefig('./assets/merge_insertion_sort.png')
plt.show()

