'''
벨만포드 알고리즘의 목적: 시작 노드로부터 모든 노드까지의 최단 경로를 찾는 것이었음!!
이를 위해 각 노드까지의 최단 거리를 추정하고 거리를 개선해나가는 로직
모든 간선에 대하여 가중치를 계산, 비교 연산을 매번하는 것이 포인트
음의 가중치 순회면 [-1]이 반환됨

다익스트라와 달리 간선 가중치가 음수일 수 있기 때문에, 우선순위큐가 아니라 모든 간선을 여러 번 반복해서 relax하는 방식 사용!
return 형식: [dist, pred]

'''

def solution(graph, source):
    n = len(graph) # 그래프 노드 수 
    INF = 10**18
    
    # 1) 거리 배열 초기화
    dist = [INF]*n          # 최단 거리 저장
    pred = [None]*n         # 경로 복원용(직전 노드 머였는지)
    dist[source] = 0
    pred[source] = None
    
    # 2) (N-1)번 모든 edge(u->v)를 relax하기
    for _ in range(n-1):
        for u in range(n):
            # 아직 u에 도착 못했으면 u에서 출발하는 간선은 의미 없으므로
            if dist[u] == INF:
                continue
            
            for v, w in graph[u]:
                new_cost = dist[u] + w
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    pred[v] = u

    # 3) 음수 cycle 검사하기: N-1번 했는데도 한 번 더 relax되면 음수 cycle이 존재
    for u in range(n):
        if dist[u] == INF:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                return [-1]
    
    return [dist, pred]
    

# print(solution([[(1, 4), (2, 3), (4, -6 )], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)],[(2, 2)]],0)) #반환갑 : [[0, -2, -4, 3, -6], [None, 2, 4, 1, 0]]
# print(solution([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]],0)) # 반환값 : [-1]

