# [1,2,3,4] is supposed to give me [24,12,8,6] 
# its the multiplication of all the elemenst of the array except the current element

values_raw = input()
values_trim = values_raw.strip().split(",")


#method 1 by division
def array_product1(values):
    index = 0
    multiply = 1
    answer = []
    for i in range(0,len(values)):
        for j in range(len(values)):
            multiply *= int(values[j])
        num = multiply//int(values[i])
        answer.append(num)
        multiply =1 
    return answer

#method 2

print(array_product1(values_trim))