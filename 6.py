def squareOfSums(it):
    sum=0
    for i in range (1,it+1):
        sum=sum+i
    return pow(sum,2)

def sumOfSquares(it):
    sum=0
    for i in range (1,it+1):
        sum=sum+pow(i,2)
    return sum

print(squareOfSums(100)-sumOfSquares(100))
