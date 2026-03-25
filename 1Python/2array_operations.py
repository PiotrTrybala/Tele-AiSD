import array
L = array.array('d', [0.0] * 48)
L[0] = 1.0
L[1] = 2.0
sum = 3.0
i = 2

while i < 48:
    n = (L[i - 1] + L[i - 2]) / (L[i - 1] - L[i - 2])
    print(f'i: {i}, n: {n}')
    L[i] = n
    sum += n
    i += 1
    
L = sorted(L)
    
print(f'L: {L}, mean L: {sum / 48}, median L: {(L[25] + L[26]) / 2}')

counter = {}

for x in L:
    if x in counter:
        counter[x] += 1
    else:
        counter[x] = 1

for x, y in zip(counter.keys(), counter.values()):
    print(f'Count {x}: {y}')