1. 문제 입력으로 주어진 간선 목록(edge list)는 DFS에서 현재 노드에서 갈 수 있는 이웃들을 매번 찾으려면 이 edge list를 매번 계속 훑어야 함 => 따라서 이 입력 graph를 인접 리스트로 변환하자!

```
[['A','B'], ['B','C'], ['C','D'], ['D','E']]

to

A: [B]
B: [C]
C: [D]
D: [E]
E: []
```

이렇게 만들어두면 DFS에서 adj[cur]만 보면 바로 다음 후보들을 얻을 수 있다.

2. DFS 구현에 필요한 것들
- adj: 인접 리스트 (dict: node -> [neighbors])
- visited: 방문 여부(set)
- order: 방문 순서 기록(list)

3. DFS 기본 로직
- 들어오자마자 방문 체크 + 기록
- 그 노드의 이웃들을 순서대로 보면서, 안 가본 곳이면 재귀로 들어감

```python
def dfs(node):
    visited.add(node)
    order.append(node)
    for nxt in adj[node]:
        if nxt not in visited:
            dfs(nxt)
```

4. 노드 수가 최대 100이라서 재귀도 안전 

5. 현재 노드가 0,1,2..와 같은 정수가 아닌 'A', 'B'와 같은 문자열이므로, adj list를 리스트로 자료구조로 선언하게 되면 (`adj = []`) 모든 노드를 모은 다음, 'A'->0, 'B'->1 이렇게 mapping을 해준 뒤에, 그 정수 인덱스로 adj list를 구성해야 함. 따라서 이 문자열 노드 문제에서는 dict를 사용했다.

- **defaultdict는 처음 봐서 찾아봄!**
`defaultdict(list)`: key가 없으면 자동으로 빈 리스트를 만들어주는 dict 

```python
my_list = defaultdict(list)
print(my_list['key']) # output: []
my_list['key'].append(4)
print(my_list['key']) # output: [4]
```

- 즉 defaultdict는 없으면 자동 생성 / 그냥 dict는 없는 key면 직접 만들어줘야함
***********************************

6. 시간 복잡도 분석
- 노드의 개수 N / 간선의 개수 E
- adj list 생성할 때는 간선 개수만큼 연산하므로 O(E)
- 탐색 시 모든 노드를 1회 방문하므로 N번 방문
=> 총 O(N+E)

