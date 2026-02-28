import heapq

def solution(N, road, K):
    # graph 만들기
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b,c)); graph[b].append((a,c))

    # dist 초기화
    INF = 10**15
    dist = [INF] * (N+1)
    dist[1] = 0

    # heap 초기화
    heap = [(0, 1)] # (현재까지 걸린 시간, 마을 번호)

    # 다익스트라
    while heap:
        cur_time, cur_node = heapq.heappop(heap)

        if cur_time > dist[cur_node]: continue
        
        for next_node, w in graph[cur_node]:
            new_time = dist[cur_node] + w
            if new_time < dist[next_node]:
                dist[next_node] = new_time
                heapq.heappush(heap, (new_time, next_node))

    # K 이하인 마을 개수 세기 
    return sum(1 for d in dist[1:] if d <= K)

