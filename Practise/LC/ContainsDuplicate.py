def solution(nums):
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            return True
        else:
            dic[nums[i]] = 1
    return False
        
print(solution([1,2,3,1]))
print(solution([1,2,3,4]))
