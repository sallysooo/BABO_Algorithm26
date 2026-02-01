from collections import defaultdict

def solution(graph, start_node):
    
    adjacent_graph = defaultdict(list)
    nodes = set()

    for u, v in graph:
        adjacent_graph[u].append(v)
        nodes.add(u)
        nodes.add(v)

    def dfs(cur_node, visited_node):
    # 1. 현재 노드 방문 노드 리스트에 추가
    # 2. 인접 노드들의 방문 여부를 찾아봄
    # 3. 방문하지 않은 노드면 해당 노드 방문
    
        visited_node.append(cur_node)
        
        for nx_node in adjacent_graph.get(cur_node,[]):
            if nx_node not in visited_node:
                dfs(nx_node, visited_node)

    visited_node = []
    dfs(start_node, visited_node)
    return visited_node

############################################################################################
####################################### 스택으로 풀기 #########################################
############################################################################################

def solution_2(graph, start_node):
    
    adjacent_graph = defaultdict(list)
    nodes = set()

    for u, v in graph:
        adjacent_graph[u].append(v)
        nodes.add(u)
        nodes.add(v)


    stack = [start_node]
    visited_node = []
        
    # 1. 시작 노드를 스택에 넣음
    # 2. 현재 스택의 노드를 빼서 visited에 넣음
    # 3. 현재 방문한 노드의 인접 노드 중 방문하지 않은 노드를 스택에 추가
    # 4. 스택이 빌 때 까지 반복

    while stack:
        cur_node = stack.pop()
        visited_node.append(cur_node)

        for adj_node in adjacent_graph.get(cur_node, []):
            if adj_node not in visited_node:
                stack.append(adj_node)

            
    return visited_node

print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
print(solution_2([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C','F'], ['E','F']], 'A'))