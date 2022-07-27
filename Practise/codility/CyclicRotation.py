def solution(A, K):
    final = [0] * len(A)
    for i in range(len(A)):
        new = (i + K) % len(A)
        final[new] = A[i]
    return final
