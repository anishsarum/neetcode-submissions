class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_graph = {}
        adj_graph = defaultdict(list)

        for u, v, t in times:
            dist_graph[(u - 1, v - 1)] = t
            adj_graph[u - 1].append(v - 1)
        
        queue = []
        dist = []
        prev = []

        for i in range(n):
            dist.append(float('inf'))
            prev.append(None)

            if i != k - 1:
                heapq.heappush(queue, (float('inf'), i))
            else:
                heapq.heappush(queue, (0, k - 1))
        
        dist[k - 1] = 0
        
        while queue:
            _, u = heapq.heappop(queue)

            for v in adj_graph[u]:
                if dist[u] + dist_graph[(u, v)] < dist[v]:
                    dist[v] = dist[u] + dist_graph[(u, v)]
                    prev[v] = u
                    heapq.heappush(queue, (dist[v], v))

        return max(dist) if max(dist) != float('inf') else -1
