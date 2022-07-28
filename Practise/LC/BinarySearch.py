def solution(nums, target): #Returns -1 if not found
    low = 0
    high = len(nums)-1
    mid = (low + high)//2
    while low <= high:
        mid = (low + high)//2
        
        if nums[mid] == target:
            return mid
            
        elif nums[mid] < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return -1
    
        
print(solution([-1,0,3,5,9,12], 9))
print(solution([-1,0,3,5,9,12,15,17,20,35], 20))
print(solution([-1,0,3,5,9,12], 2))
