
L = [1.0, 2.0]
sum = 3.0
i = 1

while True:
    n = (L[i] + L[i - 1]) / (L[i] - L[i - 1])
    i += 1
    L.append(n)
    sum += n
    if len(L) == 48:
        break
    
print(f'L: {L}, mean L: {sum / 48}, median L: {(L[25] + L[26]) / 2}')

counter = {}

for x in L:
    if x in counter:
        counter[x] += 1
    else:
        counter[x] = 1

for x, y in zip(counter.keys(), counter.values()):
    print(f'Count {x}: {y}')