import heapq, itertools

GRAPH = {
    "S": [("A", 2), ("B", 4)],
    "A": [("C", 2), ("D", 5)],
    "B": [("C", 1), ("D", 2)],
    "C": [("G", 5)],
    "D": [("G", 2)],
    "G": []
}
HEURISTIC = {"S": 7, "A": 6, "B": 4, "C": 5, "D": 2, "G": 0}

def search(heuristic):
    counter = itertools.count()
    heap = [(heuristic["S"], 0, next(counter), "S", ["S"])]
    best = {"S": 0}
    processed, expanded = [], []
    while heap:
        f, g, _, u, path = heapq.heappop(heap)
        if g != best.get(u):
            continue
        processed.append((u, g, heuristic[u], f, path))
        if u == "G":
            return path, g, processed, expanded
        expanded.append(u)
        for v, w in GRAPH[u]:
            ng = g + w
            if ng < best.get(v, float("inf")):
                best[v] = ng
                heapq.heappush(heap, (ng + heuristic[v], ng, next(counter), v, path + [v]))
    return None, None, processed, expanded

def independent_cost(path):
    return sum(next(w for v, w in GRAPH[u] if v == path[i+1])
               for i, u in enumerate(path[:-1]))

if __name__ == "__main__":
    for name, h in [
        ("A*", HEURISTIC),
        ("UCS", {k: 0 for k in GRAPH}),
        ("A* overestimate", {**HEURISTIC, "C": 10})
    ]:
        path, cost, processed, expanded = search(h)
        print(name)
        print("path:", path)
        print("reported cost:", cost)
        print("independent cost:", independent_cost(path))
        print("processed:", [(n,g,h[n],f) for n,g,h,f,_ in processed])
        print("expanded:", expanded)
        print("expansion count:", len(expanded))
        print()
