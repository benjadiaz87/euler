#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def isPrime(number):
    if(number%2==0):
        return 0
    for i in range (2,number):
        if(number%i==0):
            return 0
    return 1

def findNPrime(number):
    prime=0
    it = 0
    while(1):
        it = it+1
        if(isPrime(it)==1):
            prime=prime+1
            if(prime == number):
                return it

print (findNPrime(10001))