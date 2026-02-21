import heapq

def dijkstra(graph, start):
    
    # 거리 테이블 만들기. 초반 거리는 모두 INF로, 시작 노드는 0으로.
    # 다음에 처리할 노드들을 (비용, 노드) 형태로 우선순위 큐 pq에 넣고
    # pq에서 비용인 최소인 노드를 계속 뽑으면서,
    # 해당 노드에서 인접 노드에 대해서 비용을 계산해서
    # 인접 노드에 대한 거리테이블 값을 갱신 가능하다면 갱신하고
    # 거리테이블 값이 바뀐 노드를 pq에 (비용, 노드) 형태로 저장
    # pq가 빌 때까지 반복
    
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    prev = {node: None for node in graph}
    prev[start] = None


    pq = [(0, start)]
    
    while pq:
        cost, u = heapq.heappop(pq)

        # 구버전이면 무시
        if cost > dist[u]:
            continue 
            
        # 해당 노드와 인접한 모든 노드를 확인하고, 갱신이 가능하다면 pq에 추가
        for v, w in graph[u].items():
            new_cost = w + cost
            
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(pq ,(new_cost, v))

    ## 경로 만들기
    ## 특정 노드에서 직전 노드를 반복해서 (None이 나올 때까지)역추적 후, 리스트를 뒤집으면 됨
    paths = {}

    for target in graph:
        path = []
        
        cur = target
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        paths[target] = path
    

    return dist, paths


print(dijkstra({'A': {'B': 9, 'C': 3}, 'B': {'A': 5},'C': {'B': 1} }, 'A'))
print(dijkstra({'A':{'B':1}, 'B':{'C':5}, 'C':{'D':1}, 'D':{}}, 'A'))