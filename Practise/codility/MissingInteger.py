def solution(A):
    x = max(A)
    if x < 1:
        return 1 #If negative, return 1, since that's highest postitive int
    
    A = set(A)
    B = set(range(1, x+1))
    D = B - A #Find the difference between the two sets

    if len(D) == 0: #If no difference, return the maximum value plus 1
        return x + 1
    else:
        return min(D) #Otherwise, return the minimum of differences
        
print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1,2,3]))
print(solution([-1, -3]))
