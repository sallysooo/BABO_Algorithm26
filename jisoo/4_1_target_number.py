def solution(numbers, target):
    n = len(numbers)

    def dfs(i, sum):
        if i == n:
            return 1 if (sum == target) else 0
        return dfs(i+1, sum + numbers[i]) + dfs(i+1, sum - numbers[i])

    return dfs(0, 0)

# print(solution([1, 1, 1, 1, 1], 3))
# print(solution([4, 1, 2, 1], 4))