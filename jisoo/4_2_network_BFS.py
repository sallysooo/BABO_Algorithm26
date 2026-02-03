# BFS ver.
from collections import deque

def solution(n, computers):
    cnt = 0
    visited = [False]*n

    def bfs(start):
        q = deque([start])
        visited[start] = True # 1) 시작 노드 방문 처리 및 큐에 삽입
        
        while q:
            cur = q.popleft()
            
            for nxt in range(n):
                if computers[cur][nxt] == 1 and not visited[nxt]:
                    visited[nxt] = True # 이웃을 방문처리하고
                    q.append(nxt)       # 해당 이웃을 큐에 삽입

    for i in range(n):
        if not visited[i]:
            cnt += 1
            bfs(i)
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


