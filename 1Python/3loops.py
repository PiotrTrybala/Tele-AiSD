import time

# generowanie tablicy liczb
L = [i for i in range(0, 100)]

times = []

for i in range(1, 100):
    s = time.time()
    # pętla w stylu C++

    for i in range(0, 100):
        L[i] += 1

    duration_cpp = time.time() - s

    # pętla po obiekcie

    s = time.time()
    for l in L:
        l += 1

    duration_object = time.time() - s

    times.append((duration_cpp, duration_object))

total_cpp_time = sum(x for x, y in times)
total_obj_time = sum(y for x, y in times)

print(f'd_cpp: {total_cpp_time / 100}, d_obj: {total_obj_time / 100}, mean (duration_cpp / duration_object):', (total_cpp_time / 100) / (total_obj_time / 100))
