import heapq
import itertools

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

WEIGHTS = {
    ("A","B"): 1,
    ("A","C"): 2,
    ("B","D"): 1,
    ("B","E"): 8,
    ("C","F"): 1,
    ("D","G"): 10,
    ("E","G"): 1,
    ("F","G"): 1,
}

def ucs(start, goal):
    counter = itertools.count()
    heap = [(0, next(counter), start, [start])]
    best = {start: 0}
    processing_order = []

    while heap:
        cost, _, node, path = heapq.heappop(heap)
        if cost != best.get(node):
            continue
        processing_order.append((node, cost, path))
        if node == goal:
            return path, cost, processing_order

        for child in GRAPH[node]:
            new_cost = cost + WEIGHTS[(node, child)]
            if new_cost < best.get(child, float("inf")):
                best[child] = new_cost
                heapq.heappush(heap, (new_cost, next(counter), child, path + [child]))

    return None, None, processing_order

def path_cost(path):
    return sum(WEIGHTS[(a,b)] for a,b in zip(path,path[1:]))

if __name__ == "__main__":
    path, cost, order = ucs("A", "G")
    print("UCS path:", path)
    print("UCS cost:", cost)
    print("Independent path cost:", path_cost(path))
    print("Processing order:", order)
