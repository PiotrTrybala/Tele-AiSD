
def is_seven_divisible(x):
    return x % 7 == 0 and x % 5 != 0

found = [str(x) for x in range(500, 3000) if is_seven_divisible(x)]
counter = 0

for i in range(len(found)):
    f = found[i]
    print(f"{f} {f.find('21')}")
    index = f.find('21')
    if index != -1:
        counter += 1
        found[i] = f.replace('21', 'XX')

print(f'counted: {counter}, found: {found}')