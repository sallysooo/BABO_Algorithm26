- 그래프에서 "연결 요소"가 몇 개인지 세는 문제!
- computers 입력 리스트를 구체적으로 이해하는 것이 포인트 -> 그림과 함께 보면 이해가 쉬웠다!
- n=3 | computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]] | return 2
    - 각 `computers[i]`는 하나의 노드이다. 즉 첫 번째 [1, 1, 0]은 1번째 노드의 연결 정보를 담은 리스트, 두 번째 [1, 1, 0]은 2번째 노드의 연결 정보, [0, 0, 1]은 세 번째 연결 정보를 담은 리스트이다.
    - computers의 각 원소들 안에 있는 원소들, 즉 `computers[i][j]`는 노드 i와 노드j의 연결 여부(0/1)을 나타낸다. 즉 첫 번째 [1, 1, 0]를 해석하면 첫 번째 노드는 자기 자신과 연결되어 있으므로 1, 두 번째 노드와 연결되어 있으므로 1, 세 번째 노드와는 연결되어 있지 있지 않으므로 0이다. 
- 즉, 지금 input값은 **"인접 행렬"**이라서 굳이 인접리스트로 변환하지 않아도 됨


- 구성 요소
    - 컴퓨터 = node
    - 연결 정보 `computers[i][j]==1` = edge
    - 네트워크 개수(`return`값) = 연결 요소의 개수
    - 그래프를 여러 덩어리로 나눴을 때 덩어리(component)가 몇 개인지 반환하기

- 아이디어: 방문하지 않은 정점을 발견할 때마다 네트워크 +1
    1. visited = [False]*n
    2. for i in range(n) loop 순회
    3. 아직 방문 안 한 노드 i를 만나면:
        - 새로운 네트워크를 하나 발견할 것이므로 cnt++
        - 그리고 i에서 DFS/BFS를 돌려서 i와 연결된 또 다른 노드들을 모두 방문 처리해주기
    - 인접행렬에서 이웃 찾기는 현재 노드 cur이 있을 때,
    ```python
    for nxt in range(n): # 인접 행렬은 row를 훑어야 이웃을 알 수 있기 때문
        if computers[cur][nxt] == 1 이고 아직 방문 안했으면 방문 후 큐/재귀
    ```

- DFS로 푸는 경우
    - dfs(cur) 함수 생성
    - visited는 boolean 리스트로 다루기
    - 일단 들어오자마자 visited에 현재 노드 cur을 방문 처리: `visited[cur] = True`
    - 그 후 cur은 자신의 모든 이웃 nxt를 방문하면서
        - 연결(1)이고 방문 안했으면(not in visited) dfs(nxt)로 더 깊이 재귀 탐색
    - dfs 자체는 "탐색"만 해도 되고 네트워크의 개수는 바깥 loop에서만 세기

- BFS로 푸는 경우
    - 큐(deque) 준비
    - 시작 노드 i를 큐에 넣고 방문 처리
    - 큐에서 꺼낸 cur에 대하여
        - for nxt in range(n) 으로 cur의 이웃들을 훑기
        - 연결(1)이고 방문 안했으면(not in visited) 방문처리 + 큐에 넣기
    - 얘도 dfs와 마찬가지로 네트워크의 개수는 바깥 loop에서만 세기

```
visited 만들기
count=0
for i in range(n):
    if not visited[i]:
        count += 1
        dfs(i) 또는 bfs(i) 호출
return count
```