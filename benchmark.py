import random
import time
import matplotlib.pyplot as plt
from kdtree import build, search

def generator(n,dimensions):
    data=[([random.uniform(0,100) for i in range(dimensions)], f"item_{j}")for j in range(n)]
    return build(data)

def search_benchmark(n,dimensions=10,runs=10):
    root=generator(n,dimensions=10)
    query=[random.uniform(0,100) for i in range(dimensions)]
    
    time_lapses=[]

    for i in range(runs):
        start=time.perf_counter()
        search(root,query)
        end=time.perf_counter()
        time_lapses.append((end-start)* 1000)

    return (sum(time_lapses)/runs)

sizes = [100, 500, 1000, 5000, 10000]#number of elements
final_time_lapses=[search_benchmark(n) for n in sizes]

#print(f"{sum(final_time_lapses)/len(final_time_lapses)} ms")

plt.plot(sizes, final_time_lapses)
plt.xlabel("number of stored vectors (N)")
plt.ylabel("average search time (ms)")
plt.grid(True, alpha=0.3)
plt.savefig("benchmark.png")
plt.show()

"""
plt.figure(figsize=(10, 6))
plt.plot(sizes, final_time_lapses, marker='o', color='#1D9E75', linewidth=2)
plt.xlabel("number of stored vectors (N)")
plt.ylabel("average search time (ms)")
plt.title("PyVector KD-Tree search time vs dataset size")
plt.grid(True, alpha=0.3)
plt.savefig("benchmark.png", dpi=150, bbox_inches='tight')
plt.show()
print("benchmark saved to benchmark.png")
"""