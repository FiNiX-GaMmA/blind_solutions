# [-2,1,-3,4,-1,2,1,-5,4] this should give an output 6
# because 4-1+2+1 = 6 and this the only sub array that gives you the max sum.

#method 1
raw_input = input()
values = raw_input.strip().split(",")
def max_sub_array(values):
    sum_ans = 0
    sum_list = []
    for i in range(len(values)-1):
        for j in range(i,len(values)-1):
            for k in range(i,j):
                sum_ans += int(values[k])
            
            
            sum_list.append(sum_ans)
            sum_ans = 0
    #answer = sorted(sum_list)
    #return answer[-1]
    return sum_list

print(max_sub_array(values))

