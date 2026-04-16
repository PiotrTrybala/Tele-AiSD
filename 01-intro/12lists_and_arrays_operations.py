
import array as arr
import time

LENGTH = 48

# using python list

list = [1.0, 2.0]

s = time.time()

i = 2
while i < LENGTH:
    element = (list[i - 1] + list[i - 2]) / (list[i - 1] - list[i - 2])
    list.append(element)
    i += 1

e = time.time() - s

middle = int(len(list) / 2)
print(f'duration list: {e}, mean list: {sum(list) / 48}, median list: {(list[middle] + list[middle + 1]) / 2}')

# using python array

s = time.time()

array = arr.array('d', [0.0] * 48)
array[0], array[1] = 1.0, 2.0
i = 2
while i < LENGTH:
    element = (array[i - 1] + array[i - 2]) / (array[i - 1] / array[i - 2])
    array[i] = element
    i += 1
    
e = time.time() - s
print(f'duration array: {e}, mean array: {sum(list) / 48}, median array: {(list[middle] + list[middle + 1]) / 2}')

# sort elements in list

list = sorted(list)
print(f'sorted list: {list}')

# count elements in array

counter = {}

for element in list:
    if element in counter:
        counter[element] += 1
    else:
        counter[element] = 1
        
for element, count in zip(counter.keys(), counter.values()):
    print(f'Count of element {element}: {count}')



# L = [1.0, 2.0]
# sum = 3.0
# i = 1

# while True:
#     n = (L[i] + L[i - 1]) / (L[i] - L[i - 1])
#     i += 1
#     L.append(n)
#     sum += n
#     if len(L) == 48:
#         break
    
# L = sorted(L)
    
# print(f'L: {L}, mean L: {sum / 48}, median L: {(L[25] + L[26]) / 2}')

# counter = {}

# for x in L:
#     if x in counter:
#         counter[x] += 1
#     else:
#         counter[x] = 1

# for x, y in zip(counter.keys(), counter.values()):
#     print(f'Count {x}: {y}')