num = 1
triangleNum = 0

def DivisorCount(numCheck):
    divisors = 0
    for x in range(1 , (numCheck + 1)):
        if (numCheck % x) == 0:
            divisors += 1
    return divisors
    
while True:
    triangleNum = triangleNum + num
    if DivisorCount(triangleNum) > 3:
        break;
    else:
        num += 1
        
print triangleNum