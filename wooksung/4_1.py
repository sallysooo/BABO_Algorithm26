# 각 원소별 +/-의 두 경우 존재. 이는 깊이 n의 이진 트리로 취급할 수 있음.
# 각 단계별 두 분기의 경우의 수를 더해 전체 경우의 수를 계산.

def solution(numbers, target):
    
    def dfs(idx, sum): # idx부터 끝까지 +/-를 선택해서 target값과 일치하게 만들 수 있는 경우의 수
        
        # 1. 종료 조건
        if idx == len(numbers):
            if sum == target:
                return 1
            else:
                return 0
            
        # 2. 분기 처리
        plus = dfs(idx+1, sum + numbers[idx])
        minus = dfs(idx+1, sum - numbers[idx])
        
        return plus + minus
    
    return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))