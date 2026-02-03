from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):

    ## 최단거리. BFS
    ## 이동 가능한 경로를 어떻게 구하냐
    
    # (안됨)
    # 1. 사각형의 테두리를 포함한 좌표 전체를 루프 돌면서 1 찍음
    # 2. 각 사각형 y좌표마다 x의 최소, 최댓값만 남기고 다 0으로 바꿈 
    
    # 1. 사각형의 테두리를 포함한 좌표 전체를 루프 돌면서 1 찍음
    # 2. 각 사각형의 테두리를 제외한 내부를 다 0으로 바꿈.
    # 3. 이후에 각 사각형의 중첩된 테두리들 중에서, 내부로 바뀌는 것들 삭제
    # 4. bfs
    
    max_x = max(max(rectangle[i][0] for i in range(len(rectangle))), max(rectangle[i][2] for i in range(len(rectangle))))
    max_y = max(max(rectangle[i][1] for i in range(len(rectangle))), max(rectangle[i][3] for i in range(len(rectangle))))
    
    grid = [[0]*(max_x+1) for i in range(max_y+1)]
    visited = [[0]*(max_x+1) for i in range(max_y+1)]
    

    for l_x, l_y, r_x, r_y in rectangle:
        for y in range(l_y, r_y+1):
            for x in range(l_x,r_x+1):
                grid[y][x] = 1
    
    for l_x, l_y, r_x, r_y in rectangle:
        for y in range(l_y+1, r_y):
            for x in range(l_x+1,r_x):
                grid[y][x] = 0
                
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
                
    # # 각 사각형별 내부를 제거해도, 여러 사각형을 합치면 내부 좌표가 남을 수 있음.
    # # 따라서 인접 좌표 중에 0이 하나라도 존재해야 얘는 테두리라고 할 수 있음.
    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         for i in range(4):
    #             nx = x + dx[i]
    #             ny = y + dy[i]
    #             if 0 <= nx < max_x+1 and 0 <= ny < max_y+1:
    #                 if grid[ny][nx] == 0:
    #                     continue
    #                 else:
    #                     grid[y][x] = 0

    
    queue = deque()
    queue.append((characterX, characterY))
    
    # 방문 시에 추가할 거리
    visited[characterY][characterX] = 0
    
    # 현재 위치에서 인접 좌표로 이동 시 3가지를 체크
    # 1. 범위 안에 있는가
    # 2. 벽이 아닌가
    # 3. 이미 방문했는가
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 1. 범위 체크 
            if 0 <= nx < max_x+1 and 0 <= ny < max_y+1:
                # 2. 인접 영역이 1인지 확인.
                if grid[ny][nx] == 1:
                    # 3. 이미 방문했었는지 확인
                    if visited[ny][nx] == 0 :
                        visited[ny][nx] = visited[y][x] + 1
                        # 4. 목적지에 도달했다면 거리 반환
                        if nx == itemX and ny == itemY:
                            return visited[ny][nx] 
                        queue.append((nx,ny))


