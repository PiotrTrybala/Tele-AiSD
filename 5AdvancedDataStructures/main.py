

import numpy as np
import json
import time
from interval_tree import IntervalTree

class Benchmark:

    def __init__(self):
        self.durations = {}

    def get_results(self, n):
        if not n in self.durations:
            return []
        return self.durations[n]

    def save_results(self, filename="benchmark_results.json"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.durations, f, indent=4, sort_keys=True)
            print(f'Written results to {filename}')
        except Exception as e:
            print(f'An error occured:', e)

    # single pass of IntervalTree structure (e.g. n = 5)
    def run_case(self, n: int):
        self.durations[n] = {}
        tree = IntervalTree()

        data = np.random.uniform(0.5, 100.0, size=n).tolist()
        # insert - record times

        insert_times = []

        for d in data:
            s = time.time()
            tree.insert(d)
            insert_times.append(time.time() - s)

        print(f'durations size = {len(insert_times)}')

        self.durations[n]['insert'] = {
            'durations': insert_times,
            'mean_duration': sum(insert_times) / len(insert_times),
            'max': max(insert_times),
            'min': min(insert_times)
        }
        # search - record times

        data = np.random.uniform(0.0, 100.0, size=n).tolist()
        print(f'data size = ', len(data))

        search_times = []

        for d in data:
            s = time.time()
            if tree.search(d):
                pass
            search_times.append(time.time() - s)


        self.durations[n]['search'] = {
            'durations': search_times,
            'mean_duration': sum(search_times) / len(search_times),
            'max': max(search_times),
            'min': min(search_times)
        }

        # min - record times
        interval_size = tree.size()
        min_times = []

        for i in range(1, interval_size):
            s = time.time()
            tree.min(i)
            min_times.append(time.time() - s)

        self.durations[n]['min'] = {
            'durations': min_times,
            'mean_duration': sum(min_times) / len(min_times),
            'max': max(min_times),
            'min': min(min_times)
        }

        # max - record times
        max_times = []

        for i in range(1, interval_size):
            s = time.time()
            tree.min(i)
            max_times.append(time.time() - s)

        self.durations[n]['max'] = {
            'durations': max_times,
            'mean_duration': sum(max_times) / len(max_times),
            'max': max(max_times),
            'min': min(max_times)
        }

    def run(self, cases):

        for case in cases:
            print(f"Running case, n={case}")
            self.run_case(case)
        print("Done!")


if __name__ == "__main__":
    bench = Benchmark()
    bench.run([25, 50, 100, 200, 1000])
    bench.save_results()