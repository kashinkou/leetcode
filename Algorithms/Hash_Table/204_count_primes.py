'''
Count the number of prime numbers less than a non-negative number, n.

'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        count = 0
        prime = [True] * (n)
        prime[0] = prime[1] = False 
        for i in range(2, int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j] = False
        return sum(prime)