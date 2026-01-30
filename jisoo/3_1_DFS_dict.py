def solution(graph, start):
    adj = {}
    
    # 그냥 dict는 이렇게 없는 key에 대한 리스트를 하나씩 만들어 주는 작업이 필요
    for src, dst in graph:
        if src not in adj:
            adj[src] = []
        adj[src].append(dst)
        
        # dst는 목적지로만 나올 수도 있으니, 조회 에러 방지용으로 빈 리스트 생성해두기
        if dst not in adj:
            adj[dst] = []
            
    # DFS 순회 결과
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