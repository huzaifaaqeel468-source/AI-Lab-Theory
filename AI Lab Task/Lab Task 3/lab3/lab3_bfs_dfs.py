from collections import deque

GRAPH = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": ["G"],
    "E": ["G"],
    "F": ["G"],
    "G": []
}

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    order = []
    while queue:
        node, path = queue.popleft()
        order.append(node)
        if node == goal:
            return path, order
        for child in GRAPH[node]:
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [child]))
    return None, order

def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()
    order = []
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        if node == goal:
            return path, order
        for child in reversed(GRAPH[node]):
            if child not in visited:
                stack.append((child, path + [child]))
    return None, order

if __name__ == "__main__":
    print("BFS:", bfs("A", "G"))
    print("DFS:", dfs("A", "G"))
