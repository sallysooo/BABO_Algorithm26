from collections import deque

def solution(maps):
    # 1) 이동할 수 있는 방향을 나타내는 배열
    move = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    
    # 2) map의 크기 저장하는 변수
    n = len(maps)
    m = len(maps[0])
    
    # 3) 거리를 저장하는 배열 dist를 -1로 초기화 (n*m)
    dist = [[-1]*m for _ in range(n)]
    
    # 4) BFS
    def dfs(start):
        q = deque([start])
        dist[start[0]][start[1]] = 1
        
        while q:
            here = q.popleft()
            
            for direction in move:
                row, column = here[0] + direction[0], here[1] + direction[1]
                
                # 4-1) 이동한 위치가 범위를 벗어난 경우 다음 방향으로 넘어가기
                if row < 0 or row >= n or column < 0 or column >= m:
                    continue
                
                # 4-2) 이동한 위치에 벽이 있으면 다음 방향으로 넘어가기 
                if maps[row][column] == 0:
                    continue
                
                # 4-3) 이동한 위치가 처음 방문하는 경우, deque에 추가하고 거리 갱신
                if dist[row][column] == -1:
                    q.append([row, column])
                    dist[row][column] = dist[here[0]][here[1]] + 1
            
        # dist에는 거리가 저장됨
        return dist 
    
    dfs([0, 0])
    
    # 목적지까지의 거리 반환, 도달 못했을 경우 -1 반환
    return dist[n-1][m-1]

