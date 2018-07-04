def isPalindrome(number):
    strnumber = str(number)
    largo = len(strnumber)
    if largo%2==0:
        for i in range (0,largo):
            if(strnumber[i]!=strnumber[largo-1]): 
                return 0
            else:
                largo = largo-1
                if(largo==0): 
                    return 1
    else: 
        return 0
        
def nNumberProduct(number):
    largestPalindrome = 0
    for i in range (pow(10,number-1),pow(10,number)):
        for j in range (pow(10,number-1),pow(10,number)):
            if isPalindrome(i*j) == 1:
                if (i*j>largestPalindrome):
                     largestPalindrome=i*j
    return largestPalindrome

print nNumberProduct(3)