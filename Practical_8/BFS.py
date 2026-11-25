def BFS(adj, start):
    v = len(adj)
    visited = [False] * v
    result = []
    queue = []
    
    visited[start] = True
    queue.append(start)

    while queue:
        curr = queue.pop(0)
        result.append(curr)

        for i in adj[curr]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
    return result

if __name__ == "__main__":
    adj = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
    start = 0
    print(BFS(adj, start))
