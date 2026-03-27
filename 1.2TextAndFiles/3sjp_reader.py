
import sys
import time

text = input("Give me a input: ")

if len(text.split(' ')) != 1:
    print("Tekst nie jest jednym wyrazem")
    sys.exit(1)

text = text.lower()

# load sjp

sjp = open('SJP.txt', 'r')

s = time.time()
dictionary = sjp.readlines()
print(f'sjp loading = {time.time() - s}')
sjp.close()

# linear searching

s = time.time()
for i in range(len(dictionary)):
    if text == dictionary[i]:
        print(f'found {text} at position {i}')
        break

print(f'sjp searching {text} = {time.time() - s}')

# using binary search (without sorting, because sjp is already sorted)

def binary_search(l, lines, left, right):
    l = l.strip().lower()
    while left < right:
        middle = left + (right - left) // 2
        if lines[middle].strip('\n') == l:
            print(f'found {l} at position {middle + 1}')
            return middle

        if lines[middle] < l:
            left = middle + 1
        else:
            right = middle - 1

    print(f'text {l} not found')
    return -1


s = time.time()
print(len(dictionary))
binary_search(text, dictionary, 0, len(dictionary) - 1)
print(f'sjp searching {text}: {time.time() - s}')
