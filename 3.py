def isPrime(number):
    if(number%2==0):
        return 0
    for i in xrange(2,number/2):
        if(number%i==0):
            return 0
    return 1

def getFactors(number):
    for i in xrange (1,number/2):
        if(number%i==0 and isPrime(i)==1):
            print("|%d|")%i
        

getFactors(600851475143)