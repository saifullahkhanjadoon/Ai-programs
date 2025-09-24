# Our graph showing connections between cities
graph = {
    'Karachi': ['Lahore', 'Faisalabad'],
    'Peshawar': ['Islamabad', 'Quetta'],
    'Quetta': ['Peshawar'],
    'Multan': ['Lahore', 'Faisalabad'],
    'Faisalabad': ['Karachi', 'Multan'],
    'Lahore': ['Islamabad', 'Karachi', 'Multan'],
    'Islamabad': ['Lahore', 'Peshawar']
}

# BFS: finds shortest path from start to goal
def bfs(graph, start, goal):
    queue = [[start]]  # Start with a queue containing a path with just the start node
    visited = set()    # Keep track of nodes we've already seen

    while queue:
        path = queue.pop(0)      # Take the first path from the queue
        node = path[-1]          # Look at the last city on this path

        if node == goal:         # If this is the city we're after, we're done!
            return path

        if node not in visited:
            visited.add(node)    # Mark this city as visited

            # Add paths to all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                new_path = list(path)  # Copy the current path
                new_path.append(neighbor)  # Add the neighbor to it
                queue.append(new_path)  # Put the new path back in the queue

    return None  # No path found if we get here

# DFS (recursive): looks for a path from start to goal
def dfs_recursive_path(graph, current_node, goal_node, visited, path):
    visited.add(current_node)  # Mark current city as visited
    path.append(current_node)  # Add it to the path we're building

    if current_node == goal_node:  # If we've reached the goal, return the path
        return path

    # Otherwise, explore each neighbor
    for neighbor in graph.get(current_node, []):
        if neighbor not in visited:
            result = dfs_recursive_path(graph, neighbor, goal_node, visited, path)
            if result is not None:  # Found a path down this route
                return result

    path.pop()  # Backtrack if this route didn't lead to the goal
    return None

start_node = 'Karachi'
goal_node = 'Islamabad'

bfs_path = bfs(graph, start_node, goal_node)
dfs_path = dfs_recursive_path(graph, start_node, goal_node, set(), [])

print("BFS Path from", start_node, "to", goal_node, ":", bfs_path)
print("DFS Path from", start_node, "to", goal_node, ":", dfs_path)
