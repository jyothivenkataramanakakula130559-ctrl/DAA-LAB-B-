import heapq
def prims_algorithm(graph):
    n=len(graph)
    visited = [False] * n
    pq=[(0,0)]
    total_cost=0
    while pq:
        cost, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                heapq.heappush(pq, (weight, neighbor))
    return total_cost
if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 3)],
        1: [(0, 4), (2, 1), (3, 2)],
        2: [(0, 3), (1, 1), (3, 5)],
        3: [(1, 2), (2, 5)]
    }
    print(prims_algorithm(graph))
    