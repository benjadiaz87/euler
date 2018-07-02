def euler1 (number):
    resultado = 0
    for i in range (0,number):
        if (i%3==0 or i%5==0): 
            resultado=resultado+i
    return resultado

print (euler1(1000))