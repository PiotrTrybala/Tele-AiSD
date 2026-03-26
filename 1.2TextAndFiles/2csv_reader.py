from orca.flat_review import Line

data = []

with open('zadanie2.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()


# filter all lines where val = ""

cleared = []
for line in data:
    columns = line.strip('\n').split(',')
    if columns[1] == "":
        continue
    cleared.append(line)

# sort, fix ids and process text

lines = []
for line in cleared:
    columns = [x.lower() for x in line.strip('\n').split(',')]
    if columns[0] == 'id': continue
    lines.append(columns)

lines.sort(key=lambda l: int(l[0]))

fixed_lines = []

for i in range(1, len(lines)):
    line = lines[i]
    line[0] = str(i)
    fixed_lines.append(",".join(line))

for line in fixed_lines:
    columns = [x.lower() for x in line.strip('\n').split(',')]
    for column in columns:
        if column[1] - column[0] == 1:
            print(f'id = {columns[0]}, word = {column}')

