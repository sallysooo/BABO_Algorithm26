from collections import defaultdict, deque

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    
    # 현재 위치까지 거리가 몇인지 나타낼 dist
    # -1로 초기화 
    dist = [[-1]*col for _ in range(row)]
    
    def bfs(start):
        q = deque([start])
        dist[start[0]][start[1]] = 1   # 시작은 1
        
        while q:
            curr = q.popleft()         # curr = 현재 위치
            
            # 현재 위치에서 갈 수 있는 방향 
            for move in [[-1,0],[1,0],[0,-1],[0,1]]:
                x = curr[0] + move[0]
                y = curr[1] + move[1]
                
                # 지도 밖으로 나가는 경우 또는 벽이 있는 경우는 패스
                if x < 0 or x >= row or y < 0 or y >= col or maps[x][y] == 0:
                    continue
                
                # 갈 수 있는 곳일 때 큐에 추가. 해당 위치 거리 +1 하기 
                if dist[x][y] == -1:
                    q.append([x, y])
                    dist[x][y] = dist[curr[0]][curr[1]] + 1
                
        return dist
    
    dist = bfs([0,0])
    
    return dist[row-1][col-1]