'''
- heap 구조로 최단 거리 관리하기
출력 모양: 리스트 [각 노드까지 최소비용 distance, 각 노드까지의 최단 경로 path 노드 리스트]
이니까 return 값은 [dist_dict, path_dict] 형태여야 할 것!

다익스트라: 지금까지 발견한 경로들 중 가장 비용이 작은 노드부터 확정해가며, 
그 노드를 거쳐 가는 경로로 이웃들의 비용을 더 줄일 수 있으면 갱신하기
- dist[x]: 시작점 -> x 최소 비용 (처음엔 무한대)
- prev[x]: 최단 경로에서 x 바로 이전의 노드 (경로 복원용)
- 우선순위 큐 (현재 비용, 노드): 가장 싼 후보를 빨리 꺼내기

'''

import heapq

def solution(graph, start):
    # 1) 모든 노드 수집 (키로만 등장하는 노드 + 이웃으로만 등장하는 노드)
    nodes = set(graph.keys())
    for u in graph:
        for v in graph[u]:
            nodes.add(v)

    # 2) dist / prev 초기화
    INF = float('inf')
    dist = {node: INF for node in nodes}
    prev = {node: None for node in nodes}
    dist[start] = 0
    prev[start] = start  # 시작점은 자기 자신

    # 3) 우선순위 큐 시작
    pq = [(0, start)]  # (현재까지 비용, 노드)

    while pq:
        cur_cost, u = heapq.heappop(pq)

        # 이미 더 좋은 값으로 처리된 적이 있으면 skip
        if cur_cost != dist[u]:
            continue

        # u의 이웃들 확인
        for v, w in graph.get(u, {}).items():
            new_cost = cur_cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                prev[v] = u
                heapq.heappush(pq, (new_cost, v))

    # 4) prev를 이용해 경로 복원하는 함수
    def build_path(target):
        # 도달 불가면 빈 리스트
        if dist[target] == INF:
            return []
        path = []
        cur = target
        while True:
            path.append(cur)
            if cur == start:
                break
            cur = prev[cur]
        path.reverse()
        return path

    paths = {node: build_path(node) for node in nodes}

    return [dist, paths]

# print(solution({'A': {'B': 9, 'C': 3},'B': {'A': 5},'C': {'B': 1}},'A'))