from collections import deque
import heapq
import math

# ---------- Graph and Heuristics ----------
graph = {
    'A': [('B', 2.2), ('E', 3.3)],
    'B': [('C', 1.8), ('F', 4.2), ('A', 2.2)],
    'C': [('D', 5.5), ('G', 1.1)],
    'E': [('A', 3.3), ('H', 2.5)],
    'D':[],
    'F': [('E', 4.2), ('B', 4.2), ('G', 3.0), ('I', 1.5)],
    'G': [('C', 1.1), ('F', 3.0), ('J', 6.0)],
    'H': [('E', 2.5), ('I', 2.1), ('K', 7.0)],
    'I': [('F', 1.5), ('H', 2.1), ('J', 3.5)],
    'J': [('G', 6.0), ('I', 3.5)],
    'K': [('H', 7.0)]
}

heuristics = {
    'A': 8.0,'B': 7.0,'C': 6.0,'D': 7.0,'E': 6.0,
    'F': 3.0,'G': 4.0,'H': 2.0,'J': 1.0,'K': 3.0,'I': 0.0
}

# ---------- Helper: reconstruct path ----------
def reconstruct_path(parent, start, goal):
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        if cur == start:
            break
        cur = parent.get(cur)
    return list(reversed(path))

# ---------- BFS (shortest path in unweighted graphs) ----------
def bfs(start, goal):
    queue = deque([start])
    parent = {start: None}
    visited = {start}
    while queue:
        node = queue.popleft()
        if node == goal:
            return reconstruct_path(parent, start, goal)
        for nbr, _ in graph[node]:
            if nbr not in visited:
                visited.add(nbr)
                parent[nbr] = node
                queue.append(nbr)
    return None

# ---------- DFS (finds *a* path, not shortest) ----------
def dfs(start, goal):
    stack = [start]
    parent = {start: None}
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return reconstruct_path(parent, start, goal)
        # push neighbors (reverse order so adjacency order respected)
        for nbr, _ in reversed(graph[node]):
            if nbr not in visited:
                parent[nbr] = node
                stack.append(nbr)
    return None

# ---------- Greedy Best-First Search ----------
def greedy_best_first(start, goal):
    open_list = [(heuristics[start], start)]
    parent = {start: None}
    visited = set()
    while open_list:
        h, node = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            return reconstruct_path(parent, start, goal)
        for nbr, _ in graph[node]:
            if nbr not in visited:
                parent[nbr] = node
                heapq.heappush(open_list, (heuristics[nbr], nbr))
    return None

# ---------- A* Search ----------
def astar(start, goal):
    open_heap = [(heuristics[start], 0, start)]
    parent = {start: None}
    g_score = {start: 0}
    closed = set()
    while open_heap:
        f, g, node = heapq.heappop(open_heap)
        if node in closed:
            continue
        if node == goal:
            return reconstruct_path(parent, start, goal), g
        closed.add(node)
        for nbr, cost in graph[node]:
            tentative_g = g + cost
            if tentative_g < g_score.get(nbr, math.inf):
                g_score[nbr] = tentative_g
                parent[nbr] = node
                f_nbr = tentative_g + heuristics[nbr]
                heapq.heappush(open_heap, (f_nbr, tentative_g, nbr))
    return None, None

# ---------- Run all ----------
start, goal = 'A', 'I'

print("BFS Path:", bfs(start, goal))
print("DFS Path:", dfs(start, goal))
print("Greedy Best-First Path:", greedy_best_first(start, goal))
astar_path, astar_cost = astar(start, goal)
print("A* Path:", astar_path, "with cost:", astar_cost)
