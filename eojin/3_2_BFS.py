# dictionary 오류 방지 - 비어있어도 오류가 나지 않도록
from collections import defaultdict, deque

def solutions(graph, start):
    # 인접리스트로 변환(초기화)
    adjList = defaultdict(list)
    for u, v in graph:
        adjList[u].append(v)
    
    # bfs
    def bfs(start):
        visited = set()
        # 큐 사용 - start 넣고 시작 (초기화)
        queue = deque([start])
        visited.add(start)
        result.append(start)

        # 큐가 비어있을때까지 돌리기 
        while queue:
            node = queue.popleft()      # 큐에서 먼저 들어온거 빼주기 
            for neighbor in adjList.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)      # 방문하지 않았음 큐에 넣어주기 
                    visited.add(neighbor)
                    result.append(neighbor)     # 바로 result로 (가장 가까운것부터)
    
    result = []
    bfs(start)
    return result

graph = [['A', 'B'], ['B', 'C'], ['C', 'D'],['D', 'E']]
start = 'A'

print(solutions(graph, start))

