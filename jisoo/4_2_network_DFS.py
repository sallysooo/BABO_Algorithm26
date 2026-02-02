# DFS ver.
def solution(n, computers):
    cnt = 0
    visited = [False]*n

    # dfs의 역할: 현재 노드 cur의 "이웃"만 확인해서 방문 안 한 이웃이면 DFS로 들어가기
    def dfs(cur):
        visited[cur] = True # 1) 들어오자마자 현재 노드를 방문 처리
        for nxt in range(n):
            # 2) 현재 노드 cur과 이웃 nxt이 서로 연결(1)이고 미방문이면 dfs로 더 탐색
            if computers[cur][nxt] == 1 and not visited[nxt]:
                dfs(nxt)

    # 분리된 네트워크가 여러 개인 경우도 고려해야 하므로, 남은 미방문 노드를 또 찾아서 다시 DFS를 시작해야 네트워크 개수 세기 가능
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(i)
    return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


