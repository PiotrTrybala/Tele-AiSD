
# Naive Pattern Searching

"""
    naive_search - perform Naive Pattern Searching
    :text - text to search through
    :pattern - text to look for in :text
    :dims - dimensions (X, Y)
"""
# pattern - text to look for

# alphabet - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}

# at - treat (i, j) as index in string
def at(s, x, i, j):
    return s[i * x + j]

def naive_search_2d(txt, pattern, text_dims, pattern_dims):
    positions = []
    text_rows, text_cols = text_dims
    pattern_rows, pattern_cols = pattern_dims

    for i in range(0, text_rows - pattern_rows + 1):
        for j in range(0, text_cols - pattern_cols + 1):
            match = True

            for pi in range(0, pattern_rows):
                for pj in range(0, pattern_cols):
                    txt_char = at(txt, text_cols, i + pi, j + pj, )
                    pat_char = at(pattern, pattern_cols, pi, pj)

                    print(f'({i}, {j}) -> ({i + pi}, {j + pj}, {txt_char}, {pat_char})')

                    if pat_char != '*' and pat_char != txt_char:
                        match = False
                        break

                if not match:
                    break

            if match:
                positions.append((i, j))
    return positions

text = ""

with open("patterns/1000_pattern.txt") as f:
    text = f.read().replace('\n', '')

print(text)

positions = naive_search_2d(text, "ABCB**C**", (1000, 1000), (3, 3))

for pos in positions:
    print(pos)

# Rabin-Karp Pattern Searching

