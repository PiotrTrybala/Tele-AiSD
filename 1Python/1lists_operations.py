
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