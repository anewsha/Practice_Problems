l = [-2, 7, 4, -3]
def maxsum(l):
    max_sum = float('-inf')
    curr_sum = 0
    for num in l:
        curr_sum = max(0, curr_sum+num) #0 7 11 8
        max_sum = max(curr_sum, max_sum)#0 7 11 11
    return max_sum
print(maxsum(l))