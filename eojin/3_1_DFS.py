# dictionary 오류 방지 - 비어있어도 오류가 나지 않도록
from collections import defaultdict 

def solutions(graph, start):
    # 인접리스트로 변환(초기화)
    adjList = defaultdict(list)
    for u, v in graph:
        adjList[u].append(v)
    
    # dfs
    def dfs(node, visited, result):
        visited.add(node)       # 방문한 노드 -> 방문 리스트
        result.append(node)     # 현재 노드 -> 결과 리스트
        # 현재 노드와 인접한 노드 순회 
        for neighbor in adjList.get(node, []):
            if neighbor not in visited:        
                dfs(neighbor, visited, result)      # 재귀 함수 활용 -> 스택 유사 
        
    visited = set() # 중복 피하기 위해서
    result = []
    dfs(start, visited, result)
    return result

graph = [['A', 'B'], ['B', 'C'], ['C', 'D'],['D', 'E']]
start = 'A'

print(solutions(graph, start))