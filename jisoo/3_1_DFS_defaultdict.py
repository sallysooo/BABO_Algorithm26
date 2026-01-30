from collections import defaultdict

def solution(graph, start):
    adj = defaultdict(list) # 입력 순서 유지한 인접리스트 생성

    for src, dst in graph:
        adj[src].append(dst)

    visited = set()
    order = []
    
    def dfs(node):
        visited.add(node)
        order.append(node)
        for nxt in adj[node]:
            if nxt not in visited:
                dfs(nxt)
    
    dfs(start)
    return order

print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A')) # 반환값 : ['A', 'B', 'C', 'D', 'E']
print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A')) # 반환값 : ['A', 'B', 'D', 'E', 'F', 'C']