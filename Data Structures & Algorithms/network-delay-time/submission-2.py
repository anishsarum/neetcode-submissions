class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u - 1].append((v - 1, t))
        
        dist = [float('inf') for _ in range(n)]
        dist[k - 1] = 0

        pq = [(0, k - 1)]
        
        while pq:
            _, u = heapq.heappop(pq)

            for v, t in graph[u]:
                if dist[u] + t < dist[v]:
                    dist[v] = dist[u] + t
                    heapq.heappush(pq, (dist[v], v))

        return max(dist) if max(dist) != float('inf') else -1
