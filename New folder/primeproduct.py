def ifprime(m):
    flag = True
    if m<1:
        return False
    if m==2:
        return True
    else:
        for i in range(3,m):
            if(m%i == 0):
                flag =False
                break
    return flag
def prime_product(n):
  
    for i in range(n):
        if ifprime(i):
            for j in range(i,n):
                if(ifprime(j) and i * j==n):
                    return True
    return False
n = int(input())
#print(ifprime(n))

print(prime_product(n))