#https://projecteuler.net/problem=9

def pitagorianTriplet(number):
    for i in range (1,number):
        for j in range (i+1, number):
                for k in range (j,number):
                    if(i*i+j*j==k*k):
                        if(i+j+k==1000):
                            return i*j*k

print(pitagorianTriplet(1000))