def solution(numbers, target):  
    answer = 0 
    
    def dfs(i, currentSum):
        nonlocal answer              # 에러 방지 
        
        if i == len(numbers):
            if currentSum == target:
                answer += 1
            return
        
        else:
            dfs(i+1, currentSum + numbers[i])
            dfs(i+1, currentSum - numbers[i])
    
    dfs(0, 0)
    
    return answer