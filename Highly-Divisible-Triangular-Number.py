num = 1
triangleNum = 0
import math
    
def DivisorCount(numCheck):
    tempNum = numCheck
    testPrime = 2
    counter = 1
    returnTotal = 1
    sqrtNum = math.sqrt(numCheck)
    while testPrime <= sqrtNum:
        if tempNum % testPrime == 0:
            counter += 1
            tempNum = tempNum / testPrime
        else:
            returnTotal = returnTotal * counter
            testPrime = NextPrime(testPrime)
            counter = 1
    return returnTotal
    
def CheckPrime(numCheck):
    i = 2
    maxCheck = math.sqrt(numCheck)
    while i <= maxCheck:
        if numCheck % i == 0:
            return 0
        i += 1
    return 1

def NextPrime(numCheck):
    i = numCheck
    while True:
        i += 1
        if(CheckPrime(i)):
            return i
            
while True:
    triangleNum = triangleNum + num
    if DivisorCount(triangleNum) > 500:
        break;
    else:
        num += 1

print triangleNum