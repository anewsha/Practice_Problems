l = [2,-3,4]
def maxsum(l):
    max_sum = float('-inf')
    
    for i in range(len(l)):
        cur_sum = 0
        for j in range(i,len(l)):
            cur_sum = cur_sum + l[j]
            if cur_sum<0:
                cur_sum = 0
            max_sum = max(max_sum,cur_sum)
    return print(max_sum)

maxsum(l)