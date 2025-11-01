import sys
from collections import deque

RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"


def read_maze(filename):
    with open(filename, "r") as f:
        return [list(line.rstrip("\n")) for line in f]
pass

def find_positions(maze):
    start = target = None
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == "S":
                start = (r, c)
            elif val == "T":
                target = (r, c)
    return start, target
pass

def get_neighbors(maze, node):
    rows, cols = len(maze), len(maze[0])
    r, c = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != "#":
            neighbors.append((nr, nc))
    return neighbors
pass

def bfs(maze, start, target):
    queue = deque([start])
    visited = {start: None}
    while queue:
        node = queue.popleft()
        if node == target:
            break
        for n in get_neighbors(maze, node):
            if n not in visited:
                visited[n] = node
                queue.append(n)
    return reconstruct_path(visited, start, target)
pass

def dfs(maze, start, target):
    stack = [start]
    visited = {start: None}
    while stack:
        node = stack.pop()
        if node == target:
            break
        for n in get_neighbors(maze, node):
            if n not in visited:
                visited[n] = node
                stack.append(n)
    return reconstruct_path(visited, start, target)
pass

def reconstruct_path(visited, start, target):
    if target not in visited:
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = visited[node]
    path.reverse()
    return path
pass

def print_maze(maze, path):
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if (r, c) in path and val not in ("S", "T"):
                print(f"{RED}*{RESET}", end="")
            elif val == "S":
                print(f"{YELLOW}S{RESET}", end="")
            elif val == "T":
                print(f"{GREEN}T{RESET}", end="")
            else:
                print(val, end="")
        print()  
pass

def main():
    if len(sys.argv) != 3:
        print("Usage: python search_maze.py [bfs|dfs] maze.txt")
        sys.exit(1)

    algorithm = sys.argv[1].lower()
    filename = sys.argv[2]

    maze = read_maze(filename)
    
    start, target = find_positions(maze)
    if not start or not target:
        print("Error: Maze must contain both 'S' and 'T'.")
        sys.exit(1)

    if algorithm == "bfs":
        path = bfs(maze, start, target)
    elif algorithm == "dfs":
        path = dfs(maze, start, target)
    else:
        print("Unknown algorithm. Use 'bfs' or 'dfs'.")
        sys.exit(1)

    if not path:
        print("No path found!")
    else:
        print_maze(maze, path)
pass

if __name__ == "__main__":
    main()
