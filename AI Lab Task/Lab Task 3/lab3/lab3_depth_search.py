GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

FOUND, CUTOFF, FAILURE = "FOUND", "CUTOFF", "FAILURE"

def dls(start, goal, limit):
    processed = []
    def visit(node, path, depth):
        processed.append((node, depth, list(path)))
        if node == goal:
            return FOUND, list(path)
        if depth == limit:
            return CUTOFF, None

        saw_cutoff = False
        for child in GRAPH[node]:
            # Path-local cycle check: do not revisit a node already on this path.
            if child in path:
                continue
            status, result = visit(child, path + [child], depth + 1)
            if status == FOUND:
                return FOUND, result
            if status == CUTOFF:
                saw_cutoff = True
        return (CUTOFF if saw_cutoff else FAILURE), None

    status, path = visit(start, [start], 0)
    return status, path, processed

def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(max_depth + 1):
        status, path, processed = dls(start, goal, limit)
        attempts.append((limit, status, path, processed))
        if status == FOUND:
            return status, path, attempts
    return status, path, attempts

if __name__ == "__main__":
    for limit in range(1, 5):
        status, path, processed = dls("A", "G", limit)
        print(f"DLS limit={limit}: {status}, path={path}")
    for max_depth in range(1, 5):
        status, path, attempts = iddfs("A", "G", max_depth)
        print(f"IDDFS max_depth={max_depth}: {status}, path={path}, limits={[a[0] for a in attempts]}")
