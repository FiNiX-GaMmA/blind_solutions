# [2,5,6,7,8,9] target_sum = 7
#find the array indices whose element adds up to be exact the taget_num

#METHOD 1




def two_sum(values,target):
    answer = []
    for i in range(len(values)-1):
        if((int(values[i])+int(values[i+1]))==target):
            answer.append(i+1)
            answer.append(i+2)
    return answer
        
user_input = input()
target_num = int(input())
values = user_input.strip().split(" ")

print(two_sum(values,target_num))

#METHOD 2
def two_sum_2(values,target):
    diff = 0
    target = target_num
    dictionary_values = {}
    for index,num in enumerate(values):
        diff = target-int(num)
        if diff in dictionary_values:
            return (dictionary_values[diff],index)
        
        dictionary_values[num] = index
        

print(two_sum_2(values,target_num))
