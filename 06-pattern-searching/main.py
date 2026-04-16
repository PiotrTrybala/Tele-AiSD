
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

                    print(f'({i}, {j}) -> ({i + pi}, {j + pj}, {txt_char}, {pat_char})')

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

D = 16 # alphabet length
Q = 101 # modulus to reduce collisions

def rk_search(txt, pattern):
    # Length of the pattern
    m = len(pat)

    # Length of the text
    n = len(txt)

    # Hash value for pattern
    p = 0

    # Hash value for current window of text
    t = 0

    # High-order digit multiplier
    h = 1

    ans = []

    # Precompute h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * D) % Q

    # Compute initial hash values for pattern and first window of text
    for i in range(m):
        p = (D * p + ord(pat[i])) % Q
        t = (D * t + ord(txt[i])) % Q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):

        # If hash values match, check characters one by one
        if p == t:
            match = True
            for j in range(m):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                ans.append(i)

        # Calculate hash value for the next window
        if i < n - m:
            t = (D * (t - ord(txt[i]) * h) + ord(txt[i + m])) % Q
            if t < 0:
                t += Q
    return ans

txt = "geeksforgeeks"
pat = "geeks"
res = rk_search(txt, pat)
print(f"Rabin Karp: searching '{pat}' in '{txt}': {res}")

# def rabin_karp_2d(txt, pattern, txt_dims, pattern_dims):
#     pass


