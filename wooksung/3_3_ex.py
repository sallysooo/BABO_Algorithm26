from collections import deque

def solution(maps):
    # 행, 열 인덱스 최댓값
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0]*m for i in range(n)]
    
    queue = deque()
    queue.append((0,0))
    # 방문 시에 추가할 거리
    visited[0][0] = 1
    
    # 현재 위치에서 인접 좌표로 이동 시 3가지를 체크
    # 1. 범위 안에 있는가
    # 2. 벽이 아닌가
    # 3. 이미 방문했는가
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 인접 영역이 벽인지 확인
                if maps[nx][ny] == 1:
                    # 방문한적이 없는지 확인
                    if visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        # 목적지에 도달했으면 거리 반환
                        if nx == n-1 and ny == m-1:
                            return visited[nx][ny]
                        queue.append((nx,ny))
            
    return -1