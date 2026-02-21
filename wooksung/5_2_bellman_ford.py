def bellman_ford(graph, source):
    
    ## graph는 리스트로, graph의 인덱스가 노드번호임.
    ## graph[0]의 값이 [(1, 4), (2, 3), (4, -6)]면, 0번 노드는 1, 2, 4번 노드와 연결되어 있고 각각의 가중치는 4, 3, -6임을 의미함.
    ## source 노드에서 각 노드의 최단거리를 포함한 리스트와 각 도착노드의 직전 노드를 담은 리스트를 반환하면 됨


    # 거리 테이블 만들고, 각 노드별 거리를 Inf로 초기화
    # 거리테이블의 source 값을 0으로 설정
    # 이전 노드 저장할 리스트도 생성
    # 거리 완화를 간선 수(len(graph)-1)만큼 반복
    # 각 반복마다 graph의 노드를 모두 
    
    dist = [float('inf')]* len(graph)
    dist[source] = 0
    prev = [None] * len(graph)

    # 완화를 N-1번 반복
    for i in range(len(graph)-1):
        # 모든 출발 노드 N개를 돈다 
        for start in range(len(graph)):
            # 각 출발 노드에서 나가는 모든 간선들을 확인
            for node, weight in graph[start]:
                # 완화 가능한 조건
                # start까지 도달이 가능하고, start를 거쳐 node로 가는 비용이 더 싸면 완화
                if dist[start] != float('inf') and dist[node] > dist[start] + weight:
                    dist[node] = dist[start] + weight
                    prev[node] = start

    # 음수 사이클 검증
    # N번째 완화를 통해 거리테이블 갱신이 가능하면, 음수 사이클 존재.
    for start in range(len(graph)):
        for node, weight in graph[start]:
            if dist[start] != float('inf') and dist[node] > dist[start] + weight:
                return [-1]

    return [dist, prev]


print(bellman_ford([[(1, 4), (2, 3), (4, -6)], [(3, 5)], [(1, 2)], [(0, 7), (2, 4)], [(2, 2)]], 0))
print(bellman_ford([[(1, 5), (2, -1)], [(2, 2)], [(3, -2)], [(0, 2), (1, 6)]], 0))