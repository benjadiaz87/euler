#The sum of the primes below 10 is 2+3+5+7=17
#Find the sum of all primes below two million
import math

def isPrime(number):
    square = int(round(math.sqrt(number)))+1
    if(number%2==0 and number!=2):
        return 0
    for i in range (2,square):
        if(number%i==0):
            return 0
    return 1

def primeSum(number):
    sum=0
    for i in range (1,number):    
        if isPrime(i)==1:
            sum=sum+i
    return sum-1


print(primeSum(2000000))