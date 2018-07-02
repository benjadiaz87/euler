#Problema 2 de Project Euler
def generateFib(first =1 , second=2):
    sum=0
    while (1):
        next = first+ second
        first = second
        second = next
        if (next%2==0): 
            sum=sum+next
        if(next>4000000): 
            return sum
       # print (" |%d|")%next

print(generateFib(1,2)+2)