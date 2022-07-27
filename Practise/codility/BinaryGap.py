def solution(N):
    x = len(max(bin(N)[2:].split("1")[:-1]))
    if x == 0:
        return 0
    return int(x)
