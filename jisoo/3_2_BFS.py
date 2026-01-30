from collections import defaultdict, deque

def solution(graph, start):
    adj = defaultdict(list)
    
    for src, dst in graph:
        adj[src].append(dst)
        # dst는 목적지로만 나와도 defaultdict를 쓰니까 adj[dst] = []로 세팅되어 있어서 안전함!
    
    visited = set([start])
    q = deque([start])
    order = []
    
    while q:
        cur = q.popleft()
        order.append(cur)
        
        for nxt in adj[cur]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    
    return order

print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)],1)) # 반환값 :[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)],1)) # 반환값 : [1, 2, 3, 4, 5, 0]

