class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0

        pq = [(0, k)]
        
        while pq:
            _, u = heapq.heappop(pq)

            for v, t in graph[u]:
                if dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t
                    heapq.heappush(pq, (dist[v], v))

        return max(dist[1:]) if max(dist[1:]) != float('inf') else -1
