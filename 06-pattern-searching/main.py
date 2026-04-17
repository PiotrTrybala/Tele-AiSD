import time

# alphabet - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F}

text = ""
with open("patterns/1000_pattern.txt") as f:
    text = f.read().replace('\n', '')

# at - treat (i, j) as index in string
def at(s, x, i, j):
    return s[i * x + j]

# Naive Pattern Searching

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

                    # print(f'({i}, {j}) -> ({i + pi}, {j + pj}, {txt_char}, {pat_char})')

                    if pat_char != '*' and pat_char != txt_char:
                        match = False
                        break

                if not match:
                    break

            if match:
                positions.append((i, j))
    return positions

# naive_positions = naive_search_2d(text, "ABCB**C**", (1000, 1000), (3, 3))
#
# for pos in naive_positions:
#     print(pos)



# Rabin-Karp Pattern Searching

# First, string Rabin-Karp

# 2D Rabin-Karp Pattern Searching - without wildcards
def rk2_search(txt, pattern, txt_dims, pattern_dims):

    txt_x, txt_y = txt_dims
    pat_x, pat_y = pattern_dims
    d1, d2 = 256, 257 # Base radix
    q = 10**9 + 7 # A large prime

    positions = []

    h1 = pow(d1, pat_y - 1, q)
    h2 = pow(d2, pat_x - 1, q)

    # Stage 1: Hash pattern rows
    pat_row_hashes = []
    for i in range(pat_x):
        row_h = 0
        for j in range(pat_y):
            row_h = (d1 * row_h + ord(pattern[i * pat_y + j])) % q
        pat_row_hashes.append(row_h)

    p_hash = 0
    for h in pat_row_hashes:
        p_hash = (d2 * p_hash + h) % q

    row_hashes = [[0] * (txt_y - pat_y + 1) for _ in range(txt_y)]

    for i in range(txt_x):
        current_row_h = 0
        for j in range(pat_y):
            current_row_h = (d1 * current_row_h + ord(txt[i * txt_y + j])) % q
        row_hashes[i][0] = current_row_h

        for j in range(1, txt_y - pat_y + 1):
            prev_char = ord(txt[i * txt_y + (j - 1)])
            next_char = ord(txt[i * txt_y + (j + pat_y - 1)])
            current_row_h = (d1 * (current_row_h - prev_char * h1) + next_char) % q
            row_hashes[i][j] = (current_row_h + q) % q

    for j in range(txt_y - pat_y + 1):
        current_col_h = 0

        for i in range(pat_x):
            current_col_h = (d2 * current_col_h + row_hashes[i][j]) % q

        if current_col_h == p_hash:
            positions.append((0, j))

        for i in range(1, txt_x - pat_x + 1):
            prev_row_h = row_hashes[i - 1][j]
            next_row_h = row_hashes[i + pat_x - 1][j]
            current_col_h = (d2 * (current_col_h - prev_row_h * h2) + next_row_h) % q
            current_col_h = (current_col_h + q) % q

            if current_col_h == p_hash:
                positions.append((i, j))

    return positions

s = time.time()
print(naive_search_2d(text, "ABCB**C**", (1000, 1000), (3, 3)))
print(f'naive search execution time: {time.time() - s:.3f}(s)')

# Hydrid Approach to Rabin-Karp in 2d

def verify_wildcard(txt, pattern, i, j, text_dims, pattern_dims):

    txt_x, txt_y= text_dims
    pat_x, pat_y = pattern_dims
    for pi in range(pat_x):
        for pj in range(pat_y):
            p_char = pattern[pi * pat_y + pj]
            if p_char != '*' and txt[(pi + i) * txt_y + (pj + j)] != p_char:
                return False
    return True

def rk2_wildcard_search(txt, pattern, text_dims, pattern_dims):

    txt_x, txt_y = text_dims
    pat_x, pat_y = pattern_dims

    d, q = 256, 10**9 + 7
    h = pow(d, pat_y - 1, q)

    pat_first_row_hash = 0
    for j in range(pat_y):
        pat_first_row_hash = (d * pat_first_row_hash + ord(pattern[j])) % q

    positions = []

    for i in range(txt_x - pat_x + 1):
        current_row_h = 0

        for j in range(pat_y):
            current_row_h = (d * current_row_h + ord(txt[i * txt_y + j])) % q

        for j in range(txt_y - pat_y + 1):
            if current_row_h == pat_first_row_hash:
                if verify_wildcard(txt, pattern, i, j, text_dims, pattern_dims):
                    positions.append((i, j))

            if j < txt_y - pat_y:
                prev_char = ord(txt[i * txt_y + j])
                next_char = ord(txt[i * txt_y + j + pat_y])
                current_row_h = (d * (current_row_h - prev_char * h) + next_char) % q
                current_row_h %= q

    return positions

s = time.time()
print(rk2_wildcard_search(text, "ABCB**C**", (1000, 1000), (3, 3)))
print(f'rk2_wildcard_search execution time: {time.time() - s:.3f}(s)')
