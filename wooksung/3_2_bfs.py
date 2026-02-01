from collections import defaultdict, deque

# 3-2. BFS

# 1. 시작 노드를 큐에 넣어준다
# 2. 인접한 노드 중 방문하지 않은 노드를 큐에 추가한다
# 3. 큐의 첫번째 노드를 빼서, visited_node에 추가한다
# 4. 큐가 빌 때 까지 반복

def solution(graph, start_node):
    
    adjacent_graph = defaultdict(list)
    nodes = set()
    
    for u, v in graph:
        adjacent_graph[u].append(v)
        nodes.add(u)
        nodes.add(v)

    queue = deque([start_node])
    visited = set([start_node])
    visited_node = []

    while queue:
        cur_node = queue.popleft()
        visited_node.append(cur_node)
        for adjacent_node in adjacent_graph.get(cur_node, []):
            if adjacent_node not in visited:
                visited.add(adjacent_node)
                queue.append(adjacent_node)

    return visited_node

print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))