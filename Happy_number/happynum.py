'''
91 = 9^2 + 1^2 = 82
82 = 8^2 + 2^2 = 64 + 4 = 68
68 = 6^2 + 8^2 =  36 + 64 = 100 
100 =  1^2 + 0^2 +0^2 = 1 
''' 
 
def digits(n):
    dig = []
    while n>0:
        dig.append(n%10)
        n = n//10
    return dig

#append to seen 
#ss = digits(n) => square and sum
# if ss == 1 or ss in set break 

def happy(n):
    seen = set()
    not_happy = False
    while n != 1:
        sum = 0
        for elem in digits(n):
            sum = sum + elem**2 
    
        n = sum
        if sum in seen:
            not_happy = True
            break 
        seen.add(sum)
    return not not_happy
print(happy(61))