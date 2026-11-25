from collections import stack
def DFS(adj, start):
    v=len(adj)
    visited = [False] * v
    result = []
    stack=[]
    visited[start] = True
    stack.append(start)

    while stack:
        start = stack.popleft()
        result.append(start)

        for i in adj[start]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
    return result

if __name__ == "__main__":
    adj = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
    start = 0
    print(DFS(adj, start))
    
