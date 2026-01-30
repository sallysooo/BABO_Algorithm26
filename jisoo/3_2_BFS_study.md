1. DFS는 깊게 들어갔다가 나오는 로직(stack/recursion)
BFS는 가까운 애들부터 먼저 들어온 노드를 먼저 처리하는 FIFO queue 사용!

```
[(1, 2), (1, 3), (2, 4), (2, 5)]

to

1: [2, 3]
2: [4, 5]
4: []
5: []
3: []
```

2. BFS 구현에 필요한 것들
- adj: 인접 리스트 (dict: node -> [neighbors])
- visited: 방문 여부(set)
- q: 큐(deque)
- order: 방문 순서 기록(list)

3. BFS 기본 로직
- start를 방문 처리한다
- start를 큐에 넣는다
- 큐가 빌 때까지 반복:
    - 큐에서 하나 꺼내서(popleft)
    - 그 노드의 이웃들을 순서대로 보면서
        - 아직 방문 안 했으면 방문 처리 + 큐에 넣기

```python
from collections import deque

def bfs(start):
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

```

- popleft()니까 deque 사용하기
- 방문 체크는 "queue에 넣을 때" 하기! (중복 삽입 방지)
    - visited를 꺼낼 때 처리하면 같은 노드가 큐에 여러 번 들어갈 수 있다.








