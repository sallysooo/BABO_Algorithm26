def solution(n, computers):    
    network_count = 0
    visited = [False] * n
    
    ## 한 컴퓨터에서 DFS로 갈 수 있는 모든 컴퓨터를 방문하면, 그들은 같은 네트워크에 포함됨. 따라서, 연결이 끊기는 지점의 수를 구하는 방향으로 생각.
    
    # 1. 첫 번째 노드 방문. 방문한 적이 없으므로(visited==False) 새 네트워크에 포함.
    # 2. 첫 번째 노드와 연결되어 있는 모드 노드들 방문 처리
    # 3. 루프를 돌면서 방문하지 않은 노드(visited=False) 발견 시 새 네트워크에 포함.
    # 4. 반복
    
    def dfs(i):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                visited[j] = True
                dfs(j)
    
    
    for i in range(n):
        if visited[i] == False:
            network_count += 1
            dfs(i)
            
    
    return network_count