class Solution(object): #Uses the Sieve Of Eratosthenes algorithm
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = 0
        return sum(primes)
