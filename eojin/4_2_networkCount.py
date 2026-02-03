from collections import defaultdict 

def solution(n, computers):
    adjList = defaultdict(list)
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                adjList[i].append(j)
    
    def dfs(node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in adjList.get(node, []):
            if neighbor not in visited:
                dfs(neighbor, visited, result)
    
    count = set()
    
    for i in range(n):
        visited = set()
        result = []
        dfs(i, visited, result)
        count.add(tuple(sorted(result)))
    
    answer = len(count)
    
    return answer